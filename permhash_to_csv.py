from permhash import functions as permhash
import subprocess
import os
import tempfile
from datetime import datetime
import csv

# Lista do przechowywania wyników permhash
permhash_results = []

# Uruchom adb, aby pobrać listę plików APK na urządzeniu
adb_process = subprocess.Popen(["adb", "shell", "su", "-c", "find / -name '*.apk'"], stdout=subprocess.PIPE)
output, _ = adb_process.communicate()

# Iteruj przez wynik, aby uzyskać ścieżki do plików APK i je pobrać bezpośrednio
for apk_path in output.decode().splitlines():
    # Wyodrębnij nazwę pliku APK
    apk_name = os.path.basename(apk_path)

    # Utwórz tymczasowy katalog na hosta, gdzie będziemy przechowywać plik APK
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Ścieżka do tymczasowego pliku APK na komputerze
        apk_on_host_path = os.path.join(tmp_dir, apk_name)

        # Pobierz plik APK z urządzenia na komputer
        subprocess.run(["adb", "pull", apk_path, apk_on_host_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Oblicz permhash dla pliku APK
        ph = permhash.permhash_apk(apk_on_host_path)
        print(f"Permhash dla {apk_name}: {ph}")

        # Dodaj wynik permhash do listy wyników wraz ze ścieżką do pliku APK
        permhash_results.append({'path': apk_path, 'apk': apk_name, 'permhash': ph})

# Uzyskaj bieżącą datę i godzinę
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Zapisz wyniki do pliku CSV z datą i godziną w nazwie
csv_file_path = f'permhash_{current_datetime}.csv'
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ['path', 'apk', 'permhash']  # Dodano 'path' jako pole
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for result in permhash_results:
        writer.writerow(result)

print(f"Wyniki zostały zapisane do {csv_file_path}")

