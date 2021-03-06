import requests
import re
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=2020%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84&oquery=%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84&tqi=hUXfelprvN8ssniIbUdssssstm8-298709"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class" : "thumb"})

for image in images:
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url  = "http://"+image_url

    print(image_url)




