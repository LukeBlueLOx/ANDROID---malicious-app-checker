import csv

# Odczytaj zawartość pliku "app_list.txt"
with open("app_list.txt", "r") as txt_file:
    lines = txt_file.read().splitlines()

# Dodaj "package_name" jako nazwę kolumny na początku listy
lines.insert(0, "package_name")

# Zapisz dane do pliku CSV
with open("app_list.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows([line.split() for line in lines])

print("Data from app_list.txt has been converted to app_list.csv with 'package_name' column.")

