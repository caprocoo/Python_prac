import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
for i in range(1,6):
    print("현재 페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=178155&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)

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
            continue
        
        name = item.find("div", attrs={"class": "name"}).get_text() # 제품명
        price = item.find("strong", attrs={"class" : "price-value"}).get_text() # 가격
        # 리뷰 1000개 이상 조회

        rate = item.find("em", attrs={"class" : "rating"})# 평점
        if "Apple" in name :
            continue
        if rate :
            rate = rate.get_text()
        else :
            continue

        rate_cnt = item.find("span", attrs={"class" : "rating-total-count"})# 평점 수
        if rate_cnt :
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else :
            continue
        link = item.find("a", attrs={"class" : "search-product-link"})["href"]
        if float(rate)>=4.5 and int(rate_cnt)>1000:
            # print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}, ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*100)



    


