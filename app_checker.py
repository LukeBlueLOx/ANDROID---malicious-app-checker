import sys

def load_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def main():
    malicious_apps = load_file("list_of_malicious_applications.txt")
    app_list = load_file("application_list.txt")

    if not malicious_apps or not app_list:
        print("Error: One or both input files not found.")
        return

    matching_apps = []

    for app in malicious_apps:
        app_package = app.split(' ', 1)[0]  # Extract the package name
        for line in app_list:
            if app_package in line:
                matching_apps.append(line)

    if matching_apps:
        for match in matching_apps:
            print("Matches found: " + match)
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()

