import subprocess
import os
import tempfile
import csv
from permhash import functions as permhash

# Docelowa lokalizacja na urządzeniu, gdzie zostaną skopiowane pliki APK
target_directory = "/sdcard/APKS/"

# Lista do przechowywania wyników permhash
permhash_results = []

# Uruchom adb, aby pobrać listę plików APK na urządzeniu
adb_process = subprocess.Popen(["adb", "shell", "su", "-c", "find / -name '*.apk'"], stdout=subprocess.PIPE)
output, _ = adb_process.communicate()

# Iteruj przez wynik, aby uzyskać ścieżki do plików APK i je skopiować
for apk_path in output.decode().splitlines():
    # Wyodrębnij nazwę pliku APK
    apk_name = os.path.basename(apk_path)

    # Pełna ścieżka do skopiowanego pliku APK na urządzeniu
    apk_on_device_path = os.path.join(target_directory, apk_name)

    # Skopiuj plik APK do docelowej lokalizacji na urządzeniu
    subprocess.run(["adb", "shell", "su", "-c", f"cp {apk_path} {target_directory}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Utwórz tymczasowy katalog na hosta, gdzie będziemy przechowywać plik APK
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Ścieżka do tymczasowego pliku APK na komputerze
        apk_on_host_path = os.path.join(tmp_dir, apk_name)

        # Pobierz plik APK z urządzenia na komputer
        subprocess.run(["adb", "pull", apk_on_device_path, apk_on_host_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Oblicz permhash dla pliku APK
        ph = permhash.permhash_apk(apk_on_host_path)
        print(f"Permhash dla {apk_name}: {ph}")

        # Dodaj wynik permhash do listy wyników
        permhash_results.append({'apk': apk_name, 'permhash': ph})
    # Usuń skopiowany plik APK z docelowej lokalizacji na urządzeniu
    subprocess.run(["adb", "shell", "su", "-c", f"rm {apk_on_device_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Zapisz wyniki do pliku CSV
csv_file_path = 'permhash_test.csv'
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ['apk', 'permhash']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for result in permhash_results:
        writer.writerow(result)

print("Wyniki zostały zapisane do permhash_test.csv")


