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


#----------------------------------------------------Description of Movies--------------------------------------------
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
director_soup = soup.select(selector="p a")
print(director_soup.g)

# Create a list
director_list = []


#----------------------------------------------------All Data Into DataFrame--------------------------------------------
movies_dict_data = {
    "Movie Name": names_list,
    "Description": Description_Series,
    "Release Date": Release_Date,
    "Genre": names_of_genre,
}

df = pd.DataFrame(movies_dict_data)
# print(df)