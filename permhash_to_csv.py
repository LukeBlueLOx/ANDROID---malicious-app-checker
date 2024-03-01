from permhash import functions as permhash
import subprocess
import os
import tempfile
from datetime import datetime
import csv
import yaml

# Prompt for root permissions
root_permissions = input("Do You Have ROOT Permissions On Your ANDROID Device? (Y/N): ")

if root_permissions.upper() == 'Y':
    # Run adb to retrieve the list of APK files on the device
    adb_command = ["adb", "shell", "su", "-c", "find / -name '*.apk'"]
else:
    # Run adb to retrieve the list of APK files on the device
    adb_command = ["adb", "shell", "find / -name '*.apk'"]

# Execute adb command
adb_process = subprocess.Popen(adb_command, stdout=subprocess.PIPE)
output, _ = adb_process.communicate()

# List to store permhash results
permhash_results = []

# Iterate through the result to get paths to APK files and download them directly
for apk_path in output.decode().splitlines():
    # Extract the APK file name
    apk_name = os.path.basename(apk_path)

    # Create a temporary directory on the host where we'll store the APK file
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Path to the temporary APK file on the computer
        apk_on_host_path = os.path.join(tmp_dir, apk_name)

        # Download the APK file from the device to the computer
        subprocess.run(["adb", "pull", apk_path, apk_on_host_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Calculate the permhash for the APK file
        ph = permhash.permhash_apk(apk_on_host_path)
        print(f"Permhash for {apk_name}: {ph}")

        # Add the permhash result to the results list along with the APK file path
        permhash_results.append({'path': apk_path, 'apk': apk_name, 'permhash': ph})

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

with open("config.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
csv1 = config_vals['current_datetime']

config_vals['previous_datetime'] = csv1
config_vals['current_datetime'] = f'permhash_{current_datetime}.csv'
with open('config.yaml', "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)

# Save the results to a CSV file with the date and time in the name
csv_file_path = f'permhash_{current_datetime}.csv'
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ['path', 'apk', 'permhash']  # Added 'path' as a field
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for result in permhash_results:
        writer.writerow(result)

print(f"Results have been saved to {csv_file_path}")

