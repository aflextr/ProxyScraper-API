import os
import requests
from bs4 import BeautifulSoup

update = "https://raw.githubusercontent.com/aflextr/ProxyScraper-API/master/myapi.py"
uplink = requests.get(update)
up = BeautifulSoup(uplink.content, "html.parser")

version = ("V0.1")

if version in up.text:
    print("Program güncel")
else:
    print("Program güncel değil")


url = "https://www.my-api.co/proxy.php"

sayac =0

sayi = int(input("kac tane cekilsin:"))

for i in range(0,sayi):
    link = requests.get(url)
    Soup = BeautifulSoup(link.content,"html.parser")
    if "passed" in link.text:  
        sayac+=1
        print(Soup)
        print("proxy :",sayac)
        dosya = open("src/regex.txt","a+")
        dosya.writelines(Soup)
        dosya.write("\n")
        dosya.close()
        os.system('cd src && bash regex.sh')    




