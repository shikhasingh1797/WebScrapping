from task_1 import scrapped
import json
from bs4 import BeautifulSoup

def all_years(movies):
    years=[]
    dict1={}
    for i in movies:
        year=[]
        for j in movies:
            if i["year"]==j["year"]:
                year.append(i)
                dict1[i["year"]]=year
    with open("task_2.json","w") as file:
        json.dump(dict1,file,indent=4)
        return dict1
year=all_years(movies=scrapped)

