adb shell pm list packages | sort > app_list.txt
python3 app_list_txt_to_csv.py
python3 app_checker.py
