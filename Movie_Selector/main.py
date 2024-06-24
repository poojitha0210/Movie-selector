import bs4
from bs4 import BeautifulSoup
import random
import requests

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(URL)
content=response.text
soup=BeautifulSoup(content,"html.parser")


movie_title=soup.find_all(name="h3",class_="title")
movies=[name.getText() for name in movie_title]
movie_names=movies[::-1]
random_selection=random.choice(movie_names)

with open("movies.txt",mode="w") as file:
    file.write(f"{random_selection}\n\n")
    for movie in movie_names:
        file.write(f"{movie}\n")





print(random_selection)