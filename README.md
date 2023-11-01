# ANDROID-malicious-app-checker

https://cert.orange.pl/aktualnosci/masz-telefon-ze-starym-androidem-uwazaj-na-wysoki-rachunek

https://niebezpiecznik.pl/post/masz-androida-sprawdz-billing

https://developer.android.com/tools/adb

* install adb package:
  
    ```
    sudo apt update
    sudo apt upgrade
    sudo apt install adb
    ```

```
git clone git@github.com:LukeBlueLOx/ANDROID-malicious-app-checker.git
```
```
adb devices
```
```
cd ANDROID-malicious-app-checker
adb shell pm list packages | sort > app_list.txt
sort -o malicious_app_list.txt malicious_app_list.txt
python3 app_checker.py
```

https://x.com/LukeBlueLOx/status/1719086390535766247?s=20

https://x.com/LukeBlueLOx/status/1719051925293867304?s=20
