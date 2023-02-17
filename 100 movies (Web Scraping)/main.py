import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
soup = BeautifulSoup(response.content, "html.parser" )

# Extract the numbers from each title using regular expressions
all_movies = soup.find_all("h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]


# Save the text of all titles to a new text file
with open("movies.txt", "w") as f:
    for movie in movies:
        f.write(f"{movie}\n")

    # for movie in movie_titles:
    #     f.write(title.text + "\n")




