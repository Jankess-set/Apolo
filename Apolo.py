import socket
import os
import sys
import requests
import json

def banner():
    os.system("figlet Pentest_Box")
    print("\033[1;33mCyber Security-RT  //  Tool version 1.0_Beta\033[0;0m")

def main():
    print("""
\033[1;33m[01]\033[0;0m \033[1;34mOpen Apolo67\033[0;0m
\033[1;33m[02]\033[0;0m \033[1;34mAvailable Tools\033[0;0m
\033[1;33m[03]\033[0;0m \033[1;34mAbout\033[0;0m
\033[1;33m[04]\033[0;0m \033[1;34mWay of use\033[0;0m
\033[1;33m[05]\033[0;0m \033[1;34mMaster group information\033[0;0m
\033[1;33m[06]\033[0;0m \033[1;34mTool function\033[0;0m
\033[1;33m[07]\033[0;0m \033[1;34mCredits\033[0;0m
\033[1;33m[00]\033[0;0m \033[1;34mExit\033[0;0m
""")

    choice = input("\033[1;31m[-]\033[0;0m \033[1;32mYour Choice_> \033[0;0m")

    if choice == "01" or choice == "1":

        print("""
\033[1;33m[A]\033[0;0m - \033[1;34mWhois\033[0;0m
\033[1;33m[B]\033[0;0m - \033[1;34mSearch Dns Server\033[0;0m
\033[1;33m[C]\033[0;0m - \033[1;34mSearch IP localization\033[0;0m
\033[1;33m[D]\033[0;0m - \033[1;34mPort Scanner\033[0;0m
""")
        aux = input("\033[1;31m[-]\033[0;0m \033[1;32mYour Choice_>\033[0;0m ")

        if aux == "A" or aux == "a":
            atk1()

        elif aux == "B" or aux == "b":
            atk2()

        elif aux == "C" or aux == "c":
            atk3()

        elif aux == "D" or aux == "d":
            atk0()


    elif choice == "02" or choice == "2":
        response2()

    elif choice == "03" or choice == "3":
        response3()

    elif choice == "04" or choice == "4":
        response4()

    elif choice == "05" or choice == "5":
        response5()

    elif choice == "06" or choice == "6":
        response6()

    elif choice == "07" or choice == "7":
        response7()

    elif choice == "00":
        response00()


def atk1():

    print("\033[1;31mLoading... Please wait!\033[0;0m")

    os.system("sleep 2")

    site = input("\033[1;31m[-]\033[0;0m \033[1;32mInsert Web Site_> \033[0;0m")

    os.system(f"whois {site}")

    ret()

def atk2():
    print("\033[1;31mLoading... Please Wait!\033[0;0m")

    os.system("sleep 1")

    ip = input("\033[1;31m[-]\033[0;0m \033[1;32mInsert DNS Server_> \033[0;0m")

    if len(ip) != 7:
        print('''
        A quantidade digitada não corresponde!
        ''')
        exit()

    response = requests.get("http://ipwhois.app/json/{}?lang=pt-BR".format(ip))

    address_data = response.json()

    if 'erro' not in address_data:
        print(' ===> IP ENCONTRADO <=== ')

        print('\033[1;32mip:\033[0;0m \033[1;33m{}\033[0;0m'.format(address_data['ip']))
        print("\033[1;32msucess:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['success']))
        print("\033[1;32mtype:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['type']))
        print("\033[1;32mcontinent:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['continent']))
        print("\033[1;32mcontinent code:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['continent_code']))
        print("\033[1;32mcountry:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['country']))
        print("\033[1;32mcountry code:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['country_code']))
        print("\033[1;32mcountry flag:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['country_flag']))
        print("\033[1;32mlat:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['latitude']))
        print("\033[1;32mlon:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data["longitude"]))

        ret()

def atk3():
    ip_input = input('\033[1;31mInput ip:_>\033[0;0m  ')

    response = requests.get("http://ip-api.com/json/{}".format(ip_input))

    address_data = response.json()

    if 'erro' not in address_data:
        print('\033[1;31m===> IP FOUND <===\033[0;0m')

        print('\033[1;32mip:\033[0;0m \033[1;33m{}\033[0;0m'.format(address_data['query']))
        print("\033[1;32mstatus:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['status']))
        print("\033[1;32mcountry:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['country']))
        print("\033[1;32mcountryCode:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['countryCode']))
        print("\033[1;32mregion:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['region']))
        print("\033[1;32mregion name:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['regionName']))
        print("\033[1;32mcity:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['city']))
        print("\033[1;32mtimezone:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['timezone']))
        print("\033[1;32mzip:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['zip']))
        print("\033[1;32mlat:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['lat']))
        print("\033[1;32mlon:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['lon']))
        print("\033[1;32misp:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['isp']))
        print("\033[1;32morg:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data['org']))
        print("\033[1;32mas:\033[0;0m \033[1;33m{}\033[0;0m".format(address_data["as"]))
        exit()
    else:
        print("\033[1;31m===> IP NOT FOUND <===\033[0;0m")

    ret()

def response2():
    print("""
\033[1;31mAvailable tools are:\033[0;0m
\033[1;33m1\033[0;0m \033[1;34mWhois\033[0;0m
\033[1;33m2\033[0;0m \033[1;34mSerach DNS Server\033[0;0m
\033[1;33m3\033[0;0m \033[1;34mSearch IP Localization\033[0;0m
""")

    ret()

def atk0():
    print("\033[1;31mLoading... Please Wait!\033[0;0m")
    os.system("sleep 2")

    ip_search_scanner = input("\033[1;31mIP Input_> \033[0;0m")

    for ports_scan in range(1, 65535):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(2)

        if s.connect_ex((ip_search_scanner, ports_scan)) == 0:
            print(f"\033[1;32mPort {ports_scan} open!\033[0;0m")
            s.close()

def response4():
    print("""
\033[1;31mWai of use\033[0;0m

\033[1;32mTo use the tool, just follow it as it is, following the order and doing what is asked!\033[0;0m
    """)

    ret()

def response5():
    print("""
\033[1;31mMaster group information\033[0;0m

\033[1;32mCyberSecurity-RT chat programming, hacking, web development and technology in general. Join Now!! we have courses, videos, classes, tips and a close-knit community that focuses on learning!\033[0;0m
    """)

    ret()

def response6():
    print("""
\033[1;31mTool Function\033[0;0m

\033[1;32mThe tool has the function of helping in a Pentest, with Whois domain verification, DNS server address lookup and IP locator!\033[0;0m
    """)

    ret()

def response7():
    print("""
\033[1;31mCrédits\033[0;0m

\033[1;32mmastermind:\033[0;0m \033[1;34mJankees\033[0;0m
\033[1;32mcreator\033[0;0m \033[1;34mJankees\033[0;0m
\033[1;32mcybersecurity creator\033[0;0m \033[1;34mSasuke\033[0;0m
    """)

    ret()

def response00():
    exit = input("\033[1;31mConfirm the exit S/ Yes N/No_>\033[0;0m ")

    if exit == "N" or exit == "n":
        os.system("sleep 1")
        main()  

    else:
        print("\033[1;31mLogout\033[0;0m ")


def response3():
    print("""
\033[1;31mAbout the tool\033[0;0m

\033[1;32mThe tool was conceived and created by Cyber Security-RT, whose function is to help in a Pentest, the tools are simple, but useful!\033[0;0m
    """)
    ret()

def ret():
    pergunt = input("\033[1;31m[-]\033[0;0m \033[1;32mContinue? Y/yes or N/no_>\033[0;0m ")
    if pergunt == "Y" or pergunt == "y":
        print("\033[1;32mPlease wait!\033[0;0m")
        os.system("sleep 2")
        os.system("clear")
        main()
    else:
        print("\033[1;31mLogout!\033[0;0m")
        os.system("sleep 1")
        os.system("clear")
  

banner()
main()
