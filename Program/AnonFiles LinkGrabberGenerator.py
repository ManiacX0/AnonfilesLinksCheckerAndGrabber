import time
import string
import random
from colorama import Fore, init
import requests
import ctypes
from discord_webhook import DiscordWebhook

good = 0
bad = 0
checked = 0
total = 0

ctypes.windll.kernel32.SetConsoleTitleW(f"Anonfiles Links Grabber | By ManiacX0")

init(autoreset=True)

print(Fore.CYAN+"""
   ___                  ____ __          __   _      __      
  / _ | ___  ___  ___  / _(_) /__ ___   / /  (_)__  / /__ ___
 / __ |/ _ \/ _ \/ _ \/ _/ / / -_|_-<  / /__/ / _ \/  '_/(_-<
/_/ |_/_//_/\___/_//_/_//_/_/\__/___/ /____/_/_//_/_/\_\/___/
                                                                       
                AnonFiles Links Generator / Grabber
       cracked.to/M4niac | t.me/x0tools - Cheap configs for OB                        

                        """)

print(Fore.GREEN + "Select the method:")
print(Fore.LIGHTGREEN_EX + "[1] Auto generate links / check")
print(Fore.LIGHTGREEN_EX + "[2] Load links from file / check")
select = int(input("\n> "))

while select <= 0:
    print(Fore.RED + "Incorrect value.")
    select = int(input("\n> "))

while select > 2:
    print(Fore.RED + "Incorrect value.")
    select = int(input("\n> "))


if select == 1:
    print(Fore.LIGHTCYAN_EX + "\nHow many links to generate ?\n")
    q = int(input("> "))
    while q <= 0:
        print(Fore.RED + "Incorrect value.")
        print(Fore.LIGHTCYAN_EX + "\nHow many links to generate ?\n")
        q = int(input("> "))

    total = q


    for g in range(q):
        links = ""
        links = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.digits) for r in range(10))

        headers = {
                'Host': 'anonfiles.com',
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
                "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                'Connection': 'keep-alive'
            }


        sess = requests.Session()
        url= f"https://anonfiles.com/{links}"
    
        req= sess.get(url, headers = headers)
        if req.status_code == 200:
            good = good + 1
            checked = checked + 1
            print(Fore.YELLOW + url)
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link found !" + "\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"Anonfiles Links Grabber | Hits: {good} | Bad: {bad} | Checked: {checked}/{total} |  By ManiacX0")
            with open ("Generated Links HITS.txt", "a") as results:
                results.write(f"https://anonfiles.com/{links}" + "\n")
            webhook = DiscordWebhook(url="", content=f'```[HIT] AnonFiles\nLink: https://anonfiles.com/{links}```')
            response = webhook.execute()

        elif req.status_code == 404:
            bad = bad + 1
            checked = checked + 1
            print(Fore.YELLOW + url)
            print(Fore.LIGHTRED_EX+ "[-] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link not found !" + "\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"Anonfiles Links Grabber | Hits: {good} | Bad: {bad} | Checked: {checked}/{total} | By ManiacX0")


elif select == 2:
    print(Fore.GREEN + "\nSelect the links format:")
    print(Fore.LIGHTGREEN_EX + "[1] Full link: https://anonfiles.com/AAAAAAAAAA or https://anonfiles.com/AAAAAAAAAA/file_name")
    print(Fore.LIGHTGREEN_EX + "[2] Link code: AAAAAAAAAA")
    selectformat = int(input("\n> "))

    while selectformat <= 0:
        print(Fore.RED + "Incorrect value.")
        selectformat = int(input("\n> "))
    while selectformat > 2:
        print(Fore.RED + "Incorrect value.")
        selectformat = int(input("\n> "))

    if selectformat == 1:
        combo = open("linksloaded.txt", "r")
        while 1:
            readl = combo.readline().split("\n")[0]
            if readl == "":
                break
            sess = requests.Session()
            url= f"{readl}"

            headers = {
                'Host': 'anonfiles.com',
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
                "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                'Connection': 'keep-alive'
            }
            req= sess.get(url, headers = headers)
            if req.status_code == 200:
                good = good + 1
                checked = checked + 1
                print(Fore.YELLOW + url)
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link found !" + "\n")
                ctypes.windll.kernel32.SetConsoleTitleW(f"Anonfiles Links Grabber | Hits: {good} | Bad: {bad} |  By ManiacX0")
                with open ("Loaded Links HITS.txt", "a") as results:
                    results.write(f"{readl}" + "\n")
                webhook = DiscordWebhook(url="", content=f'```[HIT] AnonFiles\nLink: {readl}```')
                response = webhook.execute()

            elif req.status_code == 404:
                bad = bad + 1
                checked = checked + 1
                print(Fore.YELLOW + url)
                print(Fore.LIGHTRED_EX+ "[-] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link not found !" + "\n")
                ctypes.windll.kernel32.SetConsoleTitleW(f"Anonfiles Links Grabber | Hits: {good} | Bad: {bad} | By ManiacX0")

    if selectformat == 2:
        combo = open("linksloaded.txt", "r")
        while 1:
            readl = combo.readline().split("\n")[0] 
            if readl == "":
                break
            sess = requests.Session()
            url= f"https://anonfiles.com/{readl}"

            headers = {
                'Host': 'anonfiles.com',
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
                "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                'Connection': 'keep-alive'
            }
            req= sess.get(url, headers = headers)
            if req.status_code == 200:
                good = good + 1
                print(Fore.YELLOW + url)
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link found !" + "\n")
                ctypes.windll.kernel32.SetConsoleTitleW(f"Anonfiles Links Grabber | Hits: {good} | Bad: {bad} | By ManiacX0")
                with open ("Links HITS.txt", "a") as results:
                    results.write(f"{readl}" + "\n")
                webhook = DiscordWebhook(url="", content=f'```[HIT] AnonFiles\nLink: https://anonfiles.com/{readl}```')
                response = webhook.execute()

            elif req.status_code == 404:
                bad = bad + 1
                print(Fore.YELLOW + url)
                print(Fore.LIGHTRED_EX+ "[-] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link not found !" + "\n")
                ctypes.windll.kernel32.SetConsoleTitleW(f"Anonfiles Links Grabber | Hits: {good} | Bad: {bad} | By ManiacX0")
            
print(Fore.CYAN + "Results have been saved - " + Fore.LIGHTGREEN_EX + str(good) + Fore.CYAN + " hits and " + Fore.LIGHTRED_EX + str(bad) +  Fore.CYAN + " bad !")
time.sleep(7)