import sys

def load_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def get_app_and_addresses(app_list, malicious_apps):
    app_info = {}

    for app in malicious_apps:
        app_package = app.split(' ', 1)[0]
        app_info[app_package] = {
            "name": "",
            "addresses": []
        }

    for line in app_list:
        for app_package, app_data in app_info.items():
            if app_package in line:
                app_data["name"] = line

    return app_info

def main():
    malicious_apps = load_file("malicious_app_list.txt")
    app_list = load_file("app_list.txt")

    if not malicious_apps or not app_list:
        print("Error: One or both input files not found.")
        return

    app_info = get_app_and_addresses(app_list, malicious_apps)
    found_matches = False  # Add a flag to track if any matches were found.

    for app_package, data in app_info.items():
        if data["name"]:
            found_matches = True  # Set the flag to True when a match is found.
            print("-" * 100)
            print(f"Matches found: {data['name']}")
            print("Description and recipe:")
            for line in malicious_apps:
                if app_package in line:
                    description, *addresses = line.split(' ', 1)
                    for address in addresses[0].split():
                        print(address)
            print("-" * 100)

    # Check if no matches were found and print a message.
    if not found_matches:
        print("No matches found in the input data.")

if __name__ == "__main__":
    main()

