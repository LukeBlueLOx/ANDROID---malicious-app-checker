import os
import subprocess
from permhash import functions as permhash
import csv


# Ścieżka do katalogu z pakietami aplikacji
apps_directory = "/home/blox_land/ANDROID-malicious-app-checker/source/backup/apps"

# Plik CSV, do którego zapiszemy wyniki
csv_filename = "permhash.csv"

# Funkcja do obliczenia permhash dla podanej ścieżki do pliku APK
def calculate_permhash(apk_path):
    return permhash.permhash_apk(apk_path)

# Otwórz plik CSV w trybie zapisu
with open(csv_filename, mode='w', newline='') as csvfile:
    fieldnames = ['package_name', 'permhash']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Przeszukaj katalogi z pakietami aplikacji
    for package_folder in os.listdir(apps_directory):
        package_path = os.path.join(apps_directory, package_folder)

        # Sprawdź, czy istnieje katalog "a" w folderze pakietu
        apk_folder = os.path.join(package_path, 'a')
        if not os.path.exists(apk_folder):
            print(f"Nie znaleziono katalogu 'a' w pakiecie: {package_folder}")
            continue

        # Znajdź plik base.apk w katalogu "a"
        base_apk_path = os.path.join(apk_folder, 'base.apk')

        # Oblicz permhash dla pliku base.apk
        try:
            permhash_value = calculate_permhash(base_apk_path)
            writer.writerow({'package_name': package_folder, 'permhash': permhash_value})
            print(f"Pomyślnie obliczono permhash dla: {package_folder}")
        except Exception as e:
            print(f"Błąd podczas obliczania permhash dla: {package_folder}: {str(e)}")

