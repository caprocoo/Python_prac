import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=178155&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class" : re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).get_text())
#print(items[0].find("strong", attrs={"class" : "price-value"}).get_text())

for item in items :
    # 광고 제품 제외
    sold_out = item.find("div", attrs={"class" : "out-of-stock"})
    if sold_out:
        print("  <일시 품절입니다>")
        continue
    
    name = item.find("div", attrs={"class": "name"}).get_text() # 제품명
    price = item.find("strong", attrs={"class" : "price-value"}).get_text() # 가격
    # 리뷰 1000개 이상 조회

    rate = item.find("em", attrs={"class" : "rating"})# 평점
    if "삼성" in name :
        print("<삼성 상품은 제외합니다>")
        continue
    if rate :
        rate = rate.get_text()
    else :
        print("   <평점 없는 상품 제외합니다.>")
        continue

    rate_cnt = item.find("span", attrs={"class" : "rating-total-count"})# 평점 수
    if rate_cnt :
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else :
        print("   <평점 수 없는 상품 제외합니다.>")
        continue
    if float(rate)>=4.5 and int(rate_cnt)>1000:
        print(name, price, rate, rate_cnt)

    


