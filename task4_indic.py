from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

url="https://www.flipkart.com/redmi-note-10-pro-glacial-blue-128-gb/p/itm04ba1f0aed358?pid=MOBGFDFYE7TFYZKV&lid=LSTMOBGFDFYE7TFYZKVFRRVV9&marketplace=FLIPKART&q=redmi+note+10+pro&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&fm=SEARCH&iid=12360908-c2a3-41d5-b559-fb350dda2840.MOBGFDFYE7TFYZKV.SEARCH&ppt=hp&ppn=homepage&ssid=ng4okjejdc0000001623152160795&qH=20ef7d326dcad8f3"
page=requests.get(url)

soup=BeautifulSoup(page.content,"html.parser")

def mobile():
    total=[]
    model_list=[]
    model_name=[]
    phone="Phone price:"
    price=soup.find_all("div", class_="_30jeq3")
    price_list=[]
    for i in price:
        price_list.append(i.text)
    #print("Phone price=",price_list[0])
    total.append(phone)
    total.append(price_list[0])


    model=soup.find("table",class_="_14cfVK")
    model1=model.find("tbody")
    model2=model1.find_all("tr","_1s_Smc row")
    for tr in model2:
        model_list.append(tr)
    a=model_list[1]
    for i in a:
        total.append(i.text)


    print()
    b=model_list[2]
    for i in b:
        total.append(i.text)


    print()
    c=model_list[3]
    for i in c:
        total.append(i.text)


    print()
    d=model_list[4]
    for i in d:
        total.append(i.text)
    
    print()
    e=model_list[5]
    for i in e:
        total.append(i.text)


    dic1=iter(total)
    dic2=dict(zip(dic1,dic1))
    print(dic2)

    convert=open("task_4.json","w")
    json.dump(dic2,convert,indent=4)

mobile()