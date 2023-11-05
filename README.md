# ANDROID-malicious-app-checker

"2023-11-05" - Commit: migrated txt files to csv + update malicious apps list = 368 positions.

https://www.fonearena.com/blog/376170/meta-list-of-400-malicious-android-ios-apps.html

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
    adb devices
    ```

```
git clone git@github.com:LukeBlueLOx/ANDROID-malicious-app-checker.git
cd ANDROID-malicious-app-checker
python3 -m venv ANDROID-malicious-app-checker
source ANDROID-malicious-app-checker/bin/activate
pip install -r requirements.txt
chmod u+r+x check_apps.sh
```

Then - each subsequent run of the program using the command:
```
./check_apps.sh
```

https://x.com/LukeBlueLOx/status/1719086390535766247?s=20

https://x.com/LukeBlueLOx/status/1719051925293867304?s=20
