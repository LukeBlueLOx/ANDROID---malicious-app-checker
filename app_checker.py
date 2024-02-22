import sys
import csv
import pandas as pd

def load_csv(file_name):
    data = []
    try:
        with open(file_name, "r", newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the first row with column headers
            for row in reader:
                data.append([row[0].replace("package:", "")] + row[1:])
    except FileNotFoundError:
        return []

    return data

def main():
    malicious_apps = load_csv("malicious_app_list.csv")
    app_list = load_csv("app_list.csv")

    if not malicious_apps or not app_list:
        print("Error: One or both input files not found.")
        return

    # Convert the loaded data into Pandas DataFrames
    malicious_apps_df = pd.DataFrame(malicious_apps, columns=["package_name", "name", "link1", "link2"])

    if not app_list:
        print("No matches found in the input data.")
        return

    try:
        app_list_df = pd.DataFrame(app_list, columns=["package_name"])
    except ValueError:
        print("No matches found in the input data.")
        return

    # Find matching entries based on the "package_name" column
    matches = app_list_df[app_list_df["package_name"].isin(malicious_apps_df["package_name"])]

    if not matches.empty:
        found_matches = False

        for _, row in matches.iterrows():
            package_name = row["package_name"]
            data = malicious_apps_df[malicious_apps_df["package_name"] == package_name]

            if not data.empty:
                found_matches = True
                print("-" * 100)
                print(f"Matches found: {package_name}")  # Print the name from the "app_list.csv" file
                print("Description and recipe:")
                print(f"Name: {data.iloc[0]['name']}")
                print(f"Link 1: {data.iloc[0]['link1']}")
                print(f"Link 2: {data.iloc[0]['link2']}")
                print("-" * 100)

        if not found_matches:
            print("No matches found in the input data.")
    else:
        print("No matches found in the input data.")

if __name__ == "__main__":
    main()

