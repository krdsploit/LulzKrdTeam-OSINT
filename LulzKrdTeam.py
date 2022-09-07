
from antigravity import geohash
from asyncio import SubprocessProtocol
from http.client import responses
from pydoc import resolve
import socket
import os
import subprocess
import json
from urllib import response
import requests
from colorama import Fore, Back, Style
import time

time.sleep(0.10)


banner = '''



███████████████████████████████████████████████████████
█─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄─▄─█▀▀▀▀▀██▄─█─▄█▄─▄▄▀█▄─▄▄▀█
█─██─█▄▄▄▄─██─███─█▄▀─████─███████████─▄▀███─▄─▄██─██─█
▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀


$==> Title : OSINT-Krd
$==> Coder : LulzKrd Team Krd-Pentester
$==> Version : Latest 
$==> Programming Language : Python
$==> Github : github.com/krdsploit
$==> YTB : Krd Pentester


                                    '''

time.sleep(0.10)


print(Fore.YELLOW + banner)

def menu_banner():
    time.sleep(0.10)
    print(Fore.BLUE + "[*] IP OSINT [*] ")      
    time.sleep(0.10)               
    print(Fore.BLUE + "[*] Phone OSINT [*] ")  
    time.sleep(0.10)
    print(Fore.BLUE + "[*] DNS OSINT [*] ")  
    time.sleep(0.10)
    print(Fore.BLUE + "[*] Email OSINT [*] ")  
    time.sleep(0.10)
    print(Fore.BLUE + "[*] Violence OSINT [*] ")  
    time.sleep(0.10)
 

    choices_usr = int(input("Enter Your Own Choice To Pwn The Vectim $ "))

    if choices_usr==1:
        ip()
    elif choices_usr==2:
        ph()
    elif choices_usr==3:
        dns()
    elif choices_usr==8:
        email()
    elif choices_usr==9:
        email()
    elif choices_usr==10:
        vio()
    else:
        quit()


def ip():

    subprocess.call(['clear'])

    time.sleep(0.12)

    banner_ip  = '''





███████████████████████████████████████████████
█▄─▄█▄─▄▄─█▀▀▀▀▀██─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄─▄─█
██─███─▄▄▄████████─██─█▄▄▄▄─██─███─█▄▀─████─███
▀▄▄▄▀▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀
        
        
                                    '''

    print(Fore.GREEN + banner_ip)

    look_ip = input("$ ==> Enter The IP Vectime $==> ")

    url = "https://api.apilayer.com/ip_to_location/"+look_ip

    payload = {}
    headers= {
     "apikey": "iQHJExGt6zflQUsTrtDaSnwihvOI4Pe6"
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    responses = response.text
    result = json.loads(responses)
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victime City ==> " + result["city"])
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victime Location ==> " + result["continent_name"])
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victime Country Code ==> " + result["country_code"])
    time.sleep(0.12)
    print(Fore.RED   + "[+] Victime Country Name ==> " + result["country_name"])
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victime Country Name ==> " + result["continent_code"])
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victime IP Address==> " + result["ip"])
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victime Region Name ==> " + result["region_name"])
    time.sleep(0.12)
    
    warning = input("Do you want to save each information about your vectime in txt file : ")

    if warning == "Yes":
        f = open("Vec_inf", "a")
        f.write (result["city"])
        f.write (result["ip"])
        f.write (result["region_name"])
        f.write (result["country_name"])
        f.write (result["country_code"])
        f.write (result["city"])

        f.close()
    elif warning == "No":
        print("OK")


def ph():

    subprocess.call(['clear'])

    bann = '''
    
    
    
    
██████████████████████████████████████████████████████████████████
█▄─▄▄─█─█─█─▄▄─█▄─▀█▄─▄█▄─▄▄─█▀▀▀▀▀██─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄─▄─█
██─▄▄▄█─▄─█─██─██─█▄▀─███─▄█▀████████─██─█▄▄▄▄─██─███─█▄▀─████─███
▀▄▄▄▀▀▀▄▀▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀
    
    
                                            '''


    print(Fore.RED + bann)

    phone_number = input("phone:")

    url = "https://api.apilayer.com/number_verification/validate?number="+phone_number

    payload = {}
    headers= {
  "apikey": "iQHJExGt6zflQUsTrtDaSnwihvOI4Pe6"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    response = requests.request("GET", url, headers=headers, data = payload)
    responses = response.text
    result = json.loads(responses)
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victim Carrier ==> " + result["carrier"])
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victim Country ==> " + result["country_code"])
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victim  Line Type ==> " + result["line_type"])
    time.sleep(0.10)
    print(Fore.YELLOW + "[+] Victim Country Prefix ==> " + result[ "country_prefix"])
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victim Local Format ==> " + result[ "local_format"])
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victim Region Name ==> " + result["country_name"])
    time.sleep(0.12)
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victim International  ==> " + result["international_format"])
    time.sleep(0.12)
    
    



def email():

    emails = input("Email:")

    url = "https://api.apilayer.com/email_verification/check?email=email"+emails

    payload = {}
    headers= {
     "apikey": "iQHJExGt6zflQUsTrtDaSnwihvOI4Pe6"
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    responses = response.text
    result = json.loads(responses)
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victim Domain  ==> " + result ["domain"])
    time.sleep(0.12)
    print(Fore.GREEN + "[+] Victim Email ==> " + result ["email"])
    time.sleep(0.12)

    
def vio():
    
    time.sleep(0.10)


    print(Fore.YELLOW + banner)



    img_url = input("Enter The Image Url : ")


    url = "https://api.apilayer.com/violence_detection/url?url="+img_url


    payload = {}
    headers= {
    "apikey": "iQHJExGt6zflQUsTrtDaSnwihvOI4Pe6"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    responses = response.text
    results = json.loads(responses)

    print("Violence " + results['description'])
    print("Value " + (str(results['value'])))


def dns():

    domains = input("enter the domain name : ")

    url = "https://api.apilayer.com/dns_lookup/api/a/"+domains

    payload = {}
    headers= {
    "apikey": "iQHJExGt6zflQUsTrtDaSnwihvOI4Pe6"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    responses = response.text
    result = json.loads(responses)

    time.sleep(0.10)
    print(Fore.YELLOW + "[+] Victim Domain ==> " + result[ "domain"])
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victim Request Type ==> " + result["requestType"])
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victim IP Address ==> " + result["results"])
    time.sleep(0.12)
    time.sleep(0.12)
    print(Fore.YELLOW + "[+] Victim International  ==> " + result["international_format"])
    time.sleep(0.12)


if __name__ == '__main__':
    menu_banner()