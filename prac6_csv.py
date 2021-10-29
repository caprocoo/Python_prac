import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="

fileName = "시가총액1-200.csv"
fw = open(fileName, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(fw)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
print(type(title))
writer.writerow(title)


for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")
    for row in data_rows :
        colums = row.find_all("td")
        if len(colums)<=1:
            continue
        data = [column.get_text().strip() for column in colums]
        # print(data)
        writer.writerow(data)