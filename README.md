# ANDROID-malicious-app-checker

I highly recommend Ubuntu 22.04.4 LTS system:

https://ubuntu.com/download/desktop

✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌

<hr>

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
    
* If you don't have a tool installed to manage Python virtual environments and its packages, do the following:

    ```
    sudo apt install python3.10-venv
    sudo apt install python3-pip
    ```    

* Next:

    ```
    git clone https://github.com/LukeBlueLOx/ANDROID-malicious-app-checker.git
    cd ANDROID-malicious-app-checker
    python3 -m venv ANDROID-malicious-app-checker
    source ANDROID-malicious-app-checker/bin/activate
    pip install -r requirements.txt
    chmod u+r+x check_apps.sh
    chmod u+r+x permhash_and_analysis_of_changes.sh
    ```

Then - each subsequent run of the program using the command:
```
./check_apps.sh
```

Permhash and analysis of changes:
```
./permhash_and_analysis_of_changes.sh
```

And My Micro Contribution For Permhash:

https://github.com/google/permhash/issues/4

https://github.com/LukeBlueLOx/permhash/commit/523bdf68d756ac709047dd56453ad3518919a6f3

✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌

<div align="center">


Example Of Matches:

<img src="https://github.com/LukeBlueLOx/ANDROID-malicious-app-checker/blob/6be2ef81f1e4f955553b478509301b2297139c9e/Matches_Example.png" width="" height=""/>

<img src="https://github.com/LukeBlueLOx/ANDROID-malicious-app-checker/blob/6681853612087a0b1678c097e5d90a802d938bc0/Matches_Example_2024-02-22.png" width="" height=""/>
</div>

Commit "2024-02-22": update malicious apps list = 380 positions.

https://cebrf.knf.gov.pl/images/Hookbot_Builder_-_Analyze_CSIRT_KNF.pdf

https://cebrf.knf.gov.pl/komunikaty/artykuly-csirt-knf/362-ostrzezenia/858-hookbot-a-new-mobile-malware

<hr>

https://www.fonearena.com/blog/376170/meta-list-of-400-malicious-android-ios-apps.html

<hr>

https://cert.orange.pl/aktualnosci/masz-telefon-ze-starym-androidem-uwazaj-na-wysoki-rachunek

https://niebezpiecznik.pl/post/masz-androida-sprawdz-billing

<hr>

ANDROID-malicious-app-checker in social media:

https://x.com/LukeBlueLOx/status/1763638983316115866?s=20

https://m.facebook.com/story.php?story_fbid=pfbid02MLHGwxWmxw6k94utj71wyW5weF4vnWvbQXaWMYNuRsmtgQsZwdTkUFAoEAAbyNYZl&id=100069895661137

https://x.com/LukeBlueLOx/status/1719086390535766247?s=20

https://x.com/LukeBlueLOx/status/1719051925293867304?s=20
