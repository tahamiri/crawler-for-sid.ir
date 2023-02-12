#ya alireza khodet be dademoon beres
import requests
from bs4 import BeautifulSoup
import re
a = []
links = []
for i in range(1 , 166): #page ro bokon {i}
    url = f"https://sid.ir/search/paper/%D8%B1%D9%88%D8%A7%D9%86%D8%B4%D9%86%D8%A7%D8%B3%DB%8C/fa/?page={i}&sort=1&ftyp=all&fgrp=all&fyrs=1341%2c1402"

    response = requests.get(url)

    content = BeautifulSoup(response.text, "html.parser")
    
    for j in (content.find_all(attrs={"href":re.compile("/paper/\d+/fa#pointx")})):
        links.append(j.get("href"))

    
for i in range(0,len(links)):
    links[i] = "https://sid.ir"+links[i]
