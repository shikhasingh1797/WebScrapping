from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

url="https://www.nykaafashion.com/mish-maroon-solid-dress-3/p/1718483?intcmp=widget,similar_products&ppid=1429490"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
def dress():
    dic={}
    price_list=[]
    price=soup.find("span",class_="css-nt79bs e4picg41")
    store_price=price.text
    slice1=store_price[32:37]
    a=slice1
    dic["price"]=a

    colour=soup.find("div",class_="css-1ythtms ez6ebqp3")
    colour1=colour.text
    colour2=colour1[31:46]
    dic["Colour"]=colour2

    dic2={}
    select=soup.find("h2",class_="css-1bsp7u2 ex0d9t40")
    store_select=select.text
    slice2=store_select[7:11]


    size=soup.find("div",class_="css-1juqt39 esynp7i5")
    size2=size.find("button",class_="css-8h3q67 e15xcsrl0",type="button" )
    size3=size.text[2]
    em=" "
    str1=slice2+em+size3
    li=list(str1.split())

    it1=iter(li)
    zip1=dict(zip(it1,it1))
    dic.update(zip1)

    material=soup.find("div",class_="css-1mb3opd eiop2cg0")
    material1=material.text
    slice3=material1[0:8],material1[8:18]
    list1=list(slice3)
    it2=iter(list1)
    zip2=dict(zip(it2,it2))
    dic.update(zip2)

    type=soup.find_all("div",class_="css-1mb3opd eiop2cg0")

    type1=(type[1])
    type4=type1.text
    slice4=type4[0:4],type4[4:8]
    list2=list(slice4)
    it3=iter(list2)
    zip3=dict(zip(it3,it3))
    dic.update(zip3)

    occasion=(type[2])
    occasion1=occasion.text
    slice5=occasion1[0:8],occasion1[8:13]
    list3=list(slice5)
    it4=iter(list3)
    zip4=dict(zip(it4,it4))
    dic.update(zip4)

    pattern=(type[3])
    pattern1=pattern.text
    slice6=pattern1[0:7],pattern1[7:18]
    list4=list(slice6)
    it5=iter(list4)
    zip5=dict(zip(it5,it5))
    dic.update(zip5)

    fit=(type[4])
    fit1=fit.text
    slice7=fit1[0:3],fit1[3:10]
    list5=list(slice7)
    it6=iter(list5)
    zip6=dict(zip(it6,it6))
    dic.update(zip6)

    neck=(type[5])
    neck1=neck.text
    slice8=neck1[0:13],neck1[13:22]
    list6=list(slice8)
    it7=iter(list6)
    zip7=dict(zip(it7,it7))
    dic.update(zip7)

    sleeve=(type[6])
    sleeve1=sleeve.text
    slice9=sleeve1[0:11],sleeve1[11:22]
    list7=list(slice9)
    it8=iter(list7)
    zip8=dict(zip(it8,it8))
    dic.update(zip8)
    pprint(dic)

    file=open("task_6.json","w")
    json.dump(dic,file,indent=4)
    file.close()
dress()