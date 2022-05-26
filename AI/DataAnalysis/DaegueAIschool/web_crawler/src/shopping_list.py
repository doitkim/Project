# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

# BeautifulSoup : 웹페이지의 정보르 쉽게 스크랩할 수 있도록 기능을 제공 하는 라이브러리

# 키워드 input
serarch_keyword = "닭가슴살"

# 크롤링 도구
driver = webdriver.Chrome("D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\driver\chromedriver.exe")

# driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(3)
time.sleep(5)

# 오픈마켓 접속
driver.get("http://www.auction.co.kr")
time.sleep(5)

# 상품 검색 키워드
# //*[@id="txtKeyword"]
driver.find_element_by_xpath("//*[@id='txtKeyword']").send_keys(serarch_keyword)
time.sleep(2)

# //*[@id="core_header"]/div/div[1]/form/div[1]/input[2]
# 상품 키워드 검색 버튼 클릭
driver.find_element_by_xpath("//*[@id='core_header']/div/div[1]/form/div[1]/input[2]").click()

# 상품 리스트 정보 가져오기
html = driver.page_source
soup = bs(html, 'html.parser')
itemlist = soup.findAll('div', {"class": "section--itemcard"})
time.sleep(5)

title_list = []
price_list = []
link_list = []

# 가져온 상품리스트에서 필요한 상품명, 가격, 상품링크를 출력 !!
for item in itemlist:
    title = item.find("span", {"class": "text--title"}).text
    price = item.find("strong", {"class": "text--price_seller"}).text
    link = item.find("span", {"class": "text--itemcard_title ellipsis"}).a['href']

    print("상품명   : ", title)
    title_list.append(title)
    print("가격    : ", price)
    price_list.append(price)
    print("상품링크 : ", link)
    link_list.append(link)

time.sleep(3)
# print(f"title_list : {title_list}")
# print(f"price_list : {price_list}")
# print(f"link_list : {link_list}")
driver.close()

df = pd.DataFrame(title_list, columns=['상품명'])
df['가격'] = price_list
df['상품링크'] = link_list
# df.to_csv(r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\result_file\webcrawler_list.csv", index=False, encoding='utf-8')
df.to_csv(r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\result_file\webcrawler_list.csv", index=False, encoding="utf-8-sig")
# print(df)