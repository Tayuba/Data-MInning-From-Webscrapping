import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

num = [0,1,2,3,4,5,6,7,8]

dict = {
    "name": num
}

let = [ "a", "b", "c", "d", "e", "f"]

array_num = np.array(num)

df = pd.DataFrame(num, columns=["list"])
print(df)

half = []
for i in range(len(num)//2):
 print(num[i])


mat =np.array([[1,2,3],[4,6,7]])
print(mat)

page = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"

response = requests.get(page)
print(response)

soup = BeautifulSoup(response.content, "html.parser")

title_soup = soup.find_all("h3")
print(list(title_soup[0])[3].text)
