from task_2 import year
import json
from bs4 import BeautifulSoup

def group_by_decade(movies):
    dic={}
    list1=[]
    for i in movies:
        mod=i%10
        decade=i-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        dic[i]=[]
    for i in dic:
        dec=i+9
        for x in movies:
            if x<=dec and x>=i:
                for v in movies[x]:
                    dic[i].append(v)
    with open("task_3.json","w") as file:
        json.dump(dic,file,indent=4)
        return dic
print(group_by_decade(year))