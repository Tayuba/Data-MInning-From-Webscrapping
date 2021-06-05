from bs4 import BeautifulSoup
import requests
import pandas as pd

#----------------------------------------------------Data For Name Of The Movies----------------------------------------
movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
names_soup = soup.find_all(name="h3")

# create a list
names_list = []

# fill it with first 50
for idx in range(0, len(names_soup)-1):
    names_list.append(list(names_soup[idx])[3].text)

movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
names_soup = soup.find_all(name="h3")

# append the next 50
for idx in range(0, len(names_soup)-1):
    names_list.append(list(names_soup[idx])[3].text)

# Create Series file
names_series = pd.Series(names_list, name="Movie name")
print(names_series, "\n")

#----------------------------------------------------Data For Genre----------------------------------------------------
movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
movie_types_soup = soup.find_all(name="span", class_="genre")

# Create a list
names_of_genre = []

# fill it with first 50
for idx1 in range(0, len(movie_types_soup)):
    string = list(movie_types_soup[idx1])[0]
    string = string.replace("\n", "")
    names_of_genre.append(string)


movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
movie_types_soup = soup.find_all(name="span", class_="genre")

# append the next 50
for idx1 in range(0, len(movie_types_soup)):
    string = list(movie_types_soup[idx1])[0]
    string = string.replace("\n", "")
    names_of_genre.append(string)

# Create Series file
movie_types_series = pd.Series(names_of_genre, name="Genre")
print(movie_types_series, "\n")


#----------------------------------------------------Description of Movies---------------------------------------------
movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
descrip_soup = soup.find_all(name="p", class_="text-muted")


# Create a list
Discrip_list = []

# fill it with first 50
for idx in range(0, len(descrip_soup)):
    if idx % 2 != 0:
        space_out = descrip_soup[idx].text
        space_out = space_out.replace("\n", "")
        Discrip_list.append(space_out)


movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
descrip_soup = soup.find_all(name="p", class_="text-muted")

# append the next 50
for idx in range(0, len(descrip_soup)):
    if idx % 2 != 0:
        space_out = descrip_soup[idx].text
        space_out = space_out.replace("\n", "")
        Discrip_list.append(space_out)

# Create Series file
Description_Series = pd.Series(Discrip_list, name="Description")
print(Description_Series, "\n")


#----------------------------------------------------Release Date------------------------------------------------------
movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
release_soup = soup.find_all(name="span", class_="lister-item-year text-muted unbold")

# Create a list
release_date = []

# fill it with first 50
for idx in range(0, len(release_soup)):
    clean_release = release_soup[idx].text.replace("I","").replace(" ","")
    clean_release = clean_release.replace("(","").replace(")","")
    release_date.append(clean_release)


movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
release_soup = soup.find_all(name="span", class_="lister-item-year text-muted unbold")

# append the next 50
for idx in range(0, len(release_soup)):
    clean_release = release_soup[idx].text
    clean_release = clean_release.replace("(","").replace(")","")
    release_date.append(clean_release)

# Conver str to int
release_date_int = [int(i) for i in release_date]

# Create Series file
Release_Date = pd.Series(release_date_int, name="Release Date")
print(Release_Date, "\n")

#----------------------------------------------------Director Nammes----------------------------------------------------
movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
director_soup = soup.find_all(name="p", class_="")

# Create a list
director_list = []
star_list = []

# fill it with first 50
for idx in range(0, len(director_soup)):
    directors = director_soup[idx].text
    direct_star = directors.split("|")
    director1 = (direct_star[0].split(":")[1]).replace("\n","")
    director = director_list.append(director1)
    star1 = (direct_star[1].split(":")[1]).replace("\n","")
    star = star_list.append(star1)

movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# append the next 50
for idx in range(0, len(director_soup)):
    directors = director_soup[idx].text
    direct_star = directors.split("|")
    director1 = (direct_star[0].split(":")[1]).replace("\n","")
    director = director_list.append(director1)
    star1 = (direct_star[1].split(":")[1]).replace("\n","")
    star = star_list.append(star1)


# Create Series file
Director_Names = pd.Series(director_list, name="Director Names")
print(Director_Names, "\n")

# Create Series file
Star_Names = pd.Series(star_list, name="Director Names")
print(Star_Names, "\n")

#----------------------------------------------------Rating-------------------------------------------------------------
movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
rating_soup = soup.find_all(name="div", class_="inline-block ratings-imdb-rating")

rating_list =[]

# fill in first 50
for idx in range(0, len(rating_soup)):
    rating = rating_soup[idx].text
    rating = rating.replace(" ", "").replace("\n","")
    rating_list.append(rating)

movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# append the next 50
for idx in range(0, len(rating_soup)):
    rating = rating_soup[idx].text
    rating = rating.replace(" ", "").replace("\n","")
    rating_list.append(rating)

# Convert str to int
rating_list_int = [float(i) for i in rating_list]

# Create Series file
Rating = pd.Series(rating_list_int, name="Rating")
print(Rating, "\n")

#----------------------------------------------------Duration-------------------------------------------------------------
movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
duration_soup = soup.find_all(name="span", class_="runtime")

# Create a list
duration_list = []

# fill in first 50
for idx in range(0, len(duration_soup)):
    duration = duration_soup[idx].text
    duration = duration.replace("min", "")
    duration_list.append(duration)

movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# append next 50
for idx in range(0, len(duration_soup)):
    duration = duration_soup[idx].text
    duration = duration.replace("min", "")
    duration_list.append(duration)

duration_list_int = [int(i) for i in duration_list]

# Create Series file
Duration = pd.Series(duration_list_int, name="Rating")
print(Duration, "\n")
# print(duration_list_int)
#----------------------------------------------------All Data Into DataFrame--------------------------------------------
movies_dict_data = {
    "Movie Name": names_list,
    "Description": Description_Series,
    "Release Date": Release_Date,
    "Director Name": Director_Names,
    "Rating": rating_list_int,
    "Duration": Duration,
    "Genre": names_of_genre,
    "Stars(Actors)": Star_Names,
}

df = pd.DataFrame(movies_dict_data)
# print(df)
action_rows = df.loc[df["Genre"].str.contains("Action")]
# print(action_rows)

# Normalized max min (rating/

rate_dur_norm = action_rows[["Rating","Duration"]]
print(rate_dur_norm)