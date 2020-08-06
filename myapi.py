import os
import requests
from bs4 import BeautifulSoup
from torrequest import TorRequest

    
            
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
    if sayac >= 5:
        with TorRequest() as tr:
            response = tr.get('https://www.my-api.co/proxy.php')
        Soup1 = BeautifulSoup(response.content,"html.parser")
        print(Soup1)
        print("proxy :",sayac)
        dosya = open("src/regex.txt","a")
        dosya.writelines(Soup1)
        dosya.write("\n")
        dosya.close()
        os.system('cd src && bash regex.sh')
    

        
