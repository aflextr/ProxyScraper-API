import os
import requests
from bs4 import BeautifulSoup

update = "https://raw.githubusercontent.com/aflextr/ProxyScraper-API/master/proxy.py"
uplink = requests.get(update)
up = BeautifulSoup(uplink.content, "html.parser")


version = "V0.3"


if "V0.3" in up.text:
    print("Program guncel")
else:
    print("Program guncel degil")
    print("1-Guncelle.")
    print("2-Devam et.")
    secim4 = input(":")
    if secim4 =="1":
        os.system('rm -r * && git clone https://github.com/aflextr/ProxyScraper-API.git && mv ProxyScraper-API/* . && rm -r ProxyScraper-API/')
        


url1 = "https://proxy-daily.com/"

link = requests.get(url1)
Soup = BeautifulSoup(link.content, "html.parser")
payload = Soup.find("div",attrs={"class":"centeredProxyList freeProxyStyle"}).text


print("1-Normal Proxy")
print("2-Api Proxy")
print("3-Proxy list temizle")



secim = input(":")

if secim =="1":
    print(payload)
    dosyakaydet = open("list/http.txt","w")
    dosyakaydet.write(payload)
    dosyakaydet.close()
elif secim =="2":
    os.system('python3 myapi.py')
elif secim =="3":
    os.system('rm -r list/http.txt && rm -r src/regex.txt && rm -r list/apiproxy.txt')
    
print("Yakında Program güncellenecektir.")
 

