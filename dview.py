#coding=utf-8
#!/usr/bin/env python3
#SCRIPT KIDDIES NOT ALLOWED
#IF YOU COPY THIS SCRIPT PLEASE GIVE THE CREDIT TO @D3ADVAU
#@D3ADVAU
import os,sys
try:
   import requests
   from requests.structures import CaseInsensitiveDict
except:
      os.system("pip install requests")
import requests
from requests.structures import CaseInsensitiveDict
import requests,os,sys,random
os.system("clear")
logo = """
\x1b[1;92m  /$$$$$$$ \x1b[1;93m /$$    /$$\x1b[1;92m /$$$$$$\x1b[1;93m /$$$$$$$$\x1b[1;92m /$$      /$$
\x1b[1;92m | $$__  $$\x1b[1;93m| $$   | $$\x1b[1;92m|_  $$_/\x1b[1;93m| $$_____/\x1b[1;92m| $$  /$ | $$
\x1b[1;92m | $$  \ $$\x1b[1;93m| $$   | $$\x1b[1;92m  | $$  \x1b[1;93m| $$      \x1b[1;92m| $$ /$$$| $$
\x1b[1;92m | $$  | $$\x1b[1;93m|  $$ / $$/\x1b[1;92m  | $$  \x1b[1;93m| $$$$$   \x1b[1;92m| $$/$$ $$ $$
\x1b[1;92m | $$  | $$\x1b[1;93m \  $$ $$/ \x1b[1;92m  | $$  \x1b[1;93m| $$__/   \x1b[1;92m| $$$$_  $$$$
\x1b[1;92m | $$  | $$\x1b[1;93m  \  $$$/  \x1b[1;92m  | $$  \x1b[1;93m| $$      \x1b[1;92m| $$$/ \  $$$
\x1b[1;92m | $$$$$$$/\x1b[1;93m   \  $/   \x1b[1;92m /$$$$$$\x1b[1;93m| $$$$$$$$\x1b[1;92m| $$/   \  $$
\x1b[1;92m |_______/ \x1b[1;93m    \_/    \x1b[1;92m|______/\x1b[1;93m|________/\x1b[1;92m|__/     \__/\n
         \x1b[1;91mWEBSITE AUTO VISIOR MAX AMOUNT 200\n
     \x1b[1;96m╔══════════════════════════════════════════╗
     ║\x1b[1;92m  Author\x1b[1;93m     :     Dead-Man | D3ADVAU    \x1b[1;96m ║
     ║\x1b[1;92m  Github \x1b[1;93m    :     github.com/D3ADVAU    \x1b[1;96m ║
     ║\x1b[1;92m  Facebook \x1b[1;93m  :       fb.com/D3ADVAU      \x1b[1;96m ║
     ╚══════════════════════════════════════════╝
"""

def dview():
           xamn = 1
           rfr = ["facebook","google","twitter","twich","yahoo","being"]
           rfrhst = [".com",".io",".gov",".me",".net",".org",".gov.bd",".in"]
           print (logo)
           url = str(input("\x1b[1;95m  ENTER  THE URL: \x1b[1;94m"))
           amn = input("\n\x1b[1;95m  TYPE THE AMOUNT: \x1b[1;94m")
           if int(amn) < 501:
              loop = "true"
              while loop == "true":
                     if str(xamn) == str(amn):
                         loop = "false"
                     else:
                         loop = "true"
                     referer = "https://"+random.choice(rfr)+random.choice(rfrhst)
                     rsp = requests.get(url,headers={"referer": referer,"user-agent": "@D3ADVAU TRAFFIC | AUTO VISITORS FOR WEBSITE"})
                     if rsp.status_code == 200:
                         print ("\x1b[1;92m "+str(xamn)+" NO VISIT SENDING FROM "+str(referer)+"\n")
                         xamn = xamn+1
                     else:
                         print ("\x1b[1;91m  TRYING TO SEND "+str(xamn)+" TO WEBSITE\n")
           else:
               print ("  \x1b[1;91mMAX AMOUNT IS 500")
def main():
         os.system("clear")
         print (logo)
         print ("\n\x1b[1;91m  [\x1b[1;93m01\x1b[1;91m]\x1b[1;92mSTART TOOL\n\n\x1b[1;91m  [\x1b[1;93m02\x1b[1;91m]\x1b[1;92mCONTACT DEVOLOPER\n\n\x1b[1;91m  [\x1b[1;93m00\x1b[1;91m]\x1b[1;92mEXIT")
         chooseOption = input("\n\x1b[1;92m CHOOSE AN OPTION:\x1b[1;93m ")
         if chooseOption == "1" or chooseOption == "01":
            os.system("clear")
            dview()
         if chooseOption == "00" or chooseOption == "0":
            os.system("clear")
            print (logo)
            os.sys.exit()
         if chooseOption == "02" or chooseOption == "2":
            os.system("xdg-open https://facebook.com/D3ADVAU")
            main()
         else:
             print ("  \x1b[1;91mWRONG OPTION CHOOSEN PLEASE ENTER  A CORRECT OPTION")
             main()
if __name__ == "__main__":
    main()
