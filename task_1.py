from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
print(page,"***********")

soup=BeautifulSoup(page.text,"html.parser")

def scrap_top_list():
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")
    

    movie_ranks=[]
    movie_name=[]
    year_of_release=[]
    movie_urls=[]
    movie_ratings=[]

    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=""
        i=0
        while  i< len(position):
            if "." not in position[i]:
                rank=rank+position[i]
            else:
                break
            i=i+1
        movie_ranks.append(rank)

    


        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)

        year= title=tr.find("td",class_="titleColumn").span.get_text() 
        year_of_release.append(year)


        imdb_rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text() 
        movie_ratings.append(imdb_rating) 
        
        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)
    Top_movies=[]
    details={"position":"","name":"","year":"","rating":"","url":""}
    i=0
    while i<len(movie_ranks):
        
        details["position"]=int(movie_ranks[i])
        details["name"]=str(movie_name[i])
        year_of_release[i]=year_of_release[i][1:5]
        details["year"]=int(year_of_release[i])
        details["rating"]=float(movie_ratings[i])
        details["url"]=movie_urls[i]
        Top_movies.append(details)
        details={"position":"","name":"","year":"","rating":"","url":""}
        i=i+1

    with open ("task_1.json","w") as movie_data:
        json.dump(Top_movies,movie_data,indent=4)
        



    return Top_movies
scrapped=scrap_top_list()
pprint(scrap_top_list())