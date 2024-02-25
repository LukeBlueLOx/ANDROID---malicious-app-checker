import subprocess
import os
import tempfile
import csv
from permhash import functions as permhash

# Docelowa lokalizacja na urządzeniu, gdzie zostaną skopiowane pliki APK
target_directory = "/storage/C9AA-1219/"

# Lista do przechowywania wyników permhash
permhash_results = []

# Uruchom adb, aby pobrać listę pakietów
adb_process = subprocess.Popen(["adb", "shell", "pm", "list", "packages", "-f"], stdout=subprocess.PIPE)
output, _ = adb_process.communicate()

# Iteruj przez wynik adb, aby pobrać ścieżki do plików APK i je skopiować
for line in output.decode().splitlines():
    if line.startswith("package:"):
        # Wyodrębnij ścieżkę do pliku APK
        apk_path = line.split("=")[0].split(":")[1]

        # Wyodrębnij nazwę pliku APK
        apk_name = os.path.basename(apk_path)

        # Skopiuj plik APK do docelowej lokalizacji na urządzeniu
        subprocess.run(["adb", "shell", "cp", apk_path, target_directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Pełna ścieżka do skopiowanego pliku APK na urządzeniu
        apk_on_device_path = os.path.join(target_directory, apk_name)

        # Utwórz tymczasowy katalog na hosta, gdzie będziemy przechowywać plik APK
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Ścieżka do tymczasowego pliku APK na komputerze
            apk_on_host_path = os.path.join(tmp_dir, apk_name)

            # Pobierz plik APK z urządzenia na komputer
            subprocess.run(["adb", "pull", apk_on_device_path, apk_on_host_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Oblicz permhash dla pliku APK
            ph = permhash.permhash_apk(apk_on_host_path)
            print(ph)

            # Dodaj wynik permhash do listy wyników
            permhash_results.append({'APK Name': apk_name, 'Permhash': ph})

        # Usuń skopiowany plik APK z docelowej lokalizacji na urządzeniu
        subprocess.run(["adb", "shell", "rm", apk_on_device_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        #input("Naciśnij Enter, aby kontynuować...")

# Zapisz wyniki do pliku CSV
csv_file_path = 'permhash.csv'
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ['APK Name', 'Permhash']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for result in permhash_results:
        writer.writerow(result)

print("Wyniki zostały zapisane do permhash.csv")

