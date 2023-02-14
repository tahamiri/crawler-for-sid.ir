#کراولر برای سایت sid.ir
import requests
from bs4 import BeautifulSoup
import re
#تگی که در سایت سرچ کردید را در خط زیر وارد کنید
tag = "ravanshenasi"
links = []
links2 = []
#شماره اخرین صفحه تگ را به علاوه یک کنید و در ورودی دوم رنج زیر وارد کنید
for i in range(1 , 2):
    """
    لینک صفحه تگ را در خط زیر وارد کنید و این تغییر را ایجاد کنید
    page={i}
    """
    url = f"https://sid.ir/search/paper/%D8%B1%D9%88%D8%A7%D9%86%D8%B4%D9%86%D8%A7%D8%B3%DB%8C/fa/?page={i}&sort=1&ftyp=all&fgrp=all&fyrs=1341%2c1402"

    response = requests.get(url)

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
    #ادرس فایلی که میخواهید دانلود ها در انجا ذخیره شود را در خط زیر وارد کنید
    with open(f'/home/taha/Downloads/{tag}{i}.pdf', 'wb') as f:
        f.write(response.content)
