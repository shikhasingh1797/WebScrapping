from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

url="https://affyo.com/networks/gamblingpro/"
page=requests.get(url)
print(page)

soup=BeautifulSoup(page.text,"html.parser")

price=soup.find("div",id="ne-ca")
a=price.text

tracker=soup.find("table",id="ne-ov-3-ta",class_="ne-ta")
b=tracker.text

offer=soup.find("table",id="ne-ov-ta",class_="ne-ta")
c=offer.text

pay=soup.find("table",id="ne-ov-2-ta",class_="ne-ta")
d=pay.text
print(d)

slice1=a[11:17],a[17:21]
slice2=a[21:28],a[28:32]
slice3=a[32:40],a[40:44]
slice4=a[44:51],a[51:55]

slice5=a[63:68],a[69:79]
slice6=a[80:85],a[85:88]
slice7=a[88:95],a[95:98]
slice8=a[98:106],a[106:117]

slice9=b[13:31],b[31:34]

slice10=c[9:24],c[24:27],c[27:36]

slice11=c[50:66],c[66:85]
list6=list(slice11)

slice12=d[20:37],d[37:43]
slice13=d[56:62],d[61:68]
slice14=d[75:90],d[90:101]

dic1={}
add1=slice1+slice2+slice3+slice4
list1=list(add1)

add2=slice5+slice6+slice7+slice8
list2=list(add2)

list3=list(slice9)

empty=[]
list5=[]
list4=list(slice10)
list5.append(list4[0])
empty.append(list4[1])
empty.append(list4[2])
list5.append(empty)

list7=list(slice12)
empty2=[]
empty2.append(list7[1])
list7.pop(1)
list7.append(empty2)

list9=[]
list8=list(slice13)
list9=list(slice14)

it=iter(list1)
zip1=dict(zip(it,it))
dic1={}
dic1["Rating"]=zip1

it1=iter(list2)
zip2=dict(zip(it1,it1))
dic1["Contact"]=zip2

it3=iter(list3)
zip3=dict(zip(it3,it3))
dic1["Tracking"]=zip3

it4=iter(list5)
zip4=dict(zip(it4,it4))
dic1["Offers"]=zip4
dic1["Network Extra"]=list6

it5=iter(list7)
zip5=dict(zip(it5,it5))
dic1["Payment"]=zip5

zip5["Payment Delay"]=list8
zip5["Payment Method"]=list9
print(zip5)

file=open("task_5.json","w")
my_file=json.dump(dic1,file,indent=4)