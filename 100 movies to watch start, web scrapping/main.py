import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_names = [names.getText() for names in movies][::-1]

with open("top 100 movies.txt", "w") as file:
    for names in movie_names:
        file.write(names + "\n")







