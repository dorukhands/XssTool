import requests
import time
import sys
import colorama
from colorama import Fore, Back,Style
colorama.init()


header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
time.sleep(2)
print()
pog=input("POST or GET ? (p/g):")
if pog=="g":
  try:
    site=input("Site to test? (with parameters):")
    r=requests.post(site,headers=header)
    time.sleep(1)
    print()
    print(Fore.GREEN+"The site respond !"+Style.RESET_ALL)

  except:
    print()
    print("does the script respond...")
    time.sleep(3)
    print()
    print(Fore.RED+"The site doesn't respond,try again.(with https://or http://...)"+Style.RESET_ALL)
    sys.exit(0)
  print()
  try:
          wordlist=input(" wordlist directory :")
          reper=open(wordlist,"r")
  except FileNotFoundError:
      print()
      print("The File "+Fore.RED + repertoirepayload+Style.RESET_ALL +" doesn't exist, try again !")
      sys.exit(0)
  print()
  print(Fore.GREEN + "Test in process...\n")
  time.sleep(2)
  f=open(wordlist,"r")
  l=1
  for line in f:
        print()
        print(Fore.GREEN + " I test the payload " + str(1))
        if line in requests.get(site+line,headers=header).text:
            print(Fore.RED+" XSS Found Here: \n"+Style.RESET_ALL)
            print(requests.get(site+line,headers=header).url)
        else:
            print(Fore.RED + " The payload " + str(1) +" does not trigger the XSS filter."+Style.RESET_ALL)
            print()
            l+=1


elif pog=="p":
    try:
      site=input("URL to test : ")
      #data=input("Post DATA : ")
      r=requests.post(site,headers=header)
      time.sleep(1)
      print()
      print(Fore.GREEN+"The site respond !"+Style.RESET_ALL)
    except:
      print()
      print("does the script respond...")
      time.sleep(3)
      print()
      print(Fore.RED+"The site doesn't respond,try again.(with https://or http://...)"+Style.RESET_ALL)
      sys.exit(0)
      print()
    try:
              wordlist=input(" wordlist directory :")

              reper=open(wordlist,"r")
    except FileNotFoundError:
          print()
          print("The File "+Fore.RED + wordlist.txt+Style.RESET_ALL +" doesn't exist, try again !")
          sys.exit(0)
    print()
    print(Fore.GREEN + "Test in process...\n")
    time.sleep(2)
    f=open(wordlist,"r")
    l=1
    for line in f:
     print()
     print(Fore.GREEN + " I test the payload" + str(1   ))
     if line in requests.get(site+line,headers=header).text:
        print(Fore.RED+" XSS Found Here: \n"+Style.RESET_ALL)
        print(requests.get(site+line,headers=header).url)
    else:
        print(Fore.RED + " The payload" + str(1) +"does not trigger the XSS filter."+Style.RESET_ALL)
        print()
        l+=1
else:
      print("Unknow answer.")
      sys.exit(0)
