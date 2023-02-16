#کراولر برای سایت sid.ir
import requests
from bs4 import BeautifulSoup
import re

def crawl(tag, url, file_address):
    
    for j in range(0 , len(url)):
        if url[j] == "p":
            if url[j+1]=="a":
                if url[j+2]=="g":
                    if url[j+3]=="e":
                        if url[j+4]=="=":
                            new_url=url[0:j+5]+"{i}"+url[j+6:]
                            break

    links = []
    links2 = []

    response = requests.get(url)
    content = BeautifulSoup(response.text, "html.parser")
    last_page = content.find(attrs={"id":"lastpage"})
    l = last_page.get("href")
    pattern = '\d+'
    result = re.findall(pattern, l) 
    final_page = int(result[0])
    
    for i in range(1 , final_page):
                
        response = requests.get(new_url)

        content = BeautifulSoup(response.text, "html.parser")
    
        for j in (content.find_all(attrs={"href":re.compile("/paper/\d+/fa#pointx")})):
            links.append(j.get("href"))
    

    
    for i in range(0,len(links)):
        links[i] = "https://sid.ir"+links[i]

    for i in links:
        url = i
        response = requests.get(url)
        content = BeautifulSoup(response.text, "html.parser")
        for j in (content.find_all(attrs={"href":re.compile("/fileserver/jf/\d+")})):
            links2.append(j.get("href"))

    for i in range(0,len(links2)):
        links2[i] = "https://sid.ir"+links2[i]

    for i in range(0 , len(links2)):
        url = links2[i]
        response = requests.get(url)
        with open(f'{file_address}{tag}{i}.pdf', 'wb') as f:
            f.write(response.content)


crawl("ravanshenasi", "https://sid.ir/search/paper/%D8%B1%D9%88%D8%A7%D9%86%D8%B4%D9%86%D8%A7%D8%B3%DB%8C/fa/?page=1&sort=1&ftyp=all&fgrp=all&fyrs=1341%2c1402", "/home/taha/Downloads/")
