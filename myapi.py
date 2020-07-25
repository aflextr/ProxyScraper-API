import os
import requests
from bs4 import BeautifulSoup


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




