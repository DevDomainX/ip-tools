#!/usr/bin/env python3
import os 
from time import sleep
from colorama import init, Fore, Style, Back
from time import sleep

def IP():
    os.system("clear")
    while True:
        print(Fore.YELLOW+Style.BRIGHT+Back.BLUE+"""
    
        , ;-.      .           .     
        | |  )     |           |     
        | |-'  --- |-  ,-. ,-. | ,-. 
        | |        |   | | | | | `-. 
        ' '        `-' `-' `-' ' `-' 
        1LugarParaProgramar (*_-)
        
           -------- V1 ---------
    
        Created by: Hans Saldias
            """)
        title = (Fore.YELLOW+Style.BRIGHT+"""
        \n < 1 >. Information IP]
        \n < 2. > WhatmyIP
        \n < 3. > Whois
        \n < 4. > IP2Locacción
        \n < 5. > neetools 
        \n < 6. > Force  G
        \n < 7 > Look my IP
        \n < 0 >Together
        \n [ Exit ( 00 )]
        \n    """)
        for i in title:            
            print(i, end='', flush = True)
            sleep(0.1)
        try:
                
            elige = int(input("\nInsert Options: "))

            def infoip():
                ip = input("\nInsert  IP: ")
                os.system("termux-open https://ipinfo.io/"+ip))

            def WhatmyIP():
                ip = input("\nInsert  IP: ")
                os.system("termux-open https://whatismyipaddress.com/ip/"+ip)

            def whois():
                ip = input("\nInsert IP: ")
                os.system("termux-open https://whois.domaintools.com/"+ip)

            def ip2ubicación():
                ip = input("\nInsert  IP: ")
                os.system("termux-open https://www.ip2location.com/demo/"+ip)

            def nettool():
                ip = input("\nInsert  IP: ")
                os.system("termux-open https://mxtoolbox.com/SuperTool.aspx?action=arin%3a"+ip)

            def gforce():
                ip = input("\nInsert  IP: ")
                os.system("termux-open https://www.g-force.ca/en/hosting/ip-whois?ip="+ip)
        
            def verMi():
                os.system("ifconfig")
                print("where is ip ")
        
            if elige == 1:
                infoip()

            elif elige == 2:
                WhatmyIP ()

            elif elige == 3:
                whois()

            elif elige == 4:
                ip2ubicación()

            elif elige == 5:
                nettool()

            elif elige == 6:
                gforce()
        
            elif elige == 7:
                verMi()

            elif elige == 0:
                infoip()
                WhatmyIP()
                quién()
                ip2ubicación()
                red()
                gfuerza()
            elif elige == 00:
                print("1LugarParaProgramar")
                break
            else:
                print("Error write a options")
                IP()
        except ValueError:
         print("option invalide")
IP()       
     
