import os
import requests
from bs4 import BeautifulSoup

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
    os.system('rm -r list/proxy.txt src/regex.txt')
    
print("Yakında Program güncellenecektir.")
 
