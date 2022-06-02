from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
from urllib.request import (urlopen, urlparse, urlretrieve)


# 구글 이미지 URL
chrome_path = r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\driver\chromedriver.exe"
base_url = "https://www.google.co.kr/imghp"

# 구글 검색 옵션
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("lang=ko_KR")# 한국어
chrome_options.add_argument("window-size=1920x1080")

def selenium_scroll_option() :
    SCROLL_PAUSE_SEC = 1

    # 스크롤 높이 가져옴
    last_height = driver.execute_script(
        "return document.body.scrollHeight")

    while True :
        # 끝까지 스크롤 다운
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_SEC)
        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script(
            "return document.body.scrollHeight")
        if new_height == last_height :
            break
        last_height = new_height

a = "망고"
image_name = 'mango'
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.google.co.kr/imghp?hl=ko")
browser = driver.find_element_by_name('q')
browser.send_keys(a)
browser.send_keys(Keys.RETURN)

# //*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input
selenium_scroll_option()# 스크롤 하여 이미지 확보
driver.find_element_by_xpath(
    '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
selenium_scroll_option()

# 이미지 저장 src 요소를 리스트업 해서 이미지 url 저장
image = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# 클래스 네임에서 공백은 . 을 찍어줌

print(image)
image_url = []
for i in image:
    if i.get_attribute("src") != None :
        image_url.append(i.get_attribute("src"))
    else :
        image_url.append(i.get_attribute("data-src"))

# 전체 이미지 개수
print(f"전체 다운로드한 이미지 개수 : {len(image_url)}")
image_url = pd.DataFrame(image_url)[0].unique()

# 해당하는 파일에 이미지 다운로드
os.makedirs(r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\result_file\fruit\mango", exist_ok=True)
mango = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/mango/"

if image_name == 'mango' :
    for t, url in enumerate(image_url, 0) :
        urlretrieve(url, mango + image_name + "_" + str(t) + ".png")

    # driver.close()

print(mango)
print("망고 완료")

b = "Dragon fruit"
image_name = "Dragon_fruit"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.google.co.kr/imghp?hl=ko")
browser = driver.find_element_by_name('q')
browser.send_keys(b)
browser.send_keys(Keys.RETURN)

# //*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input
selenium_scroll_option()# 스크롤 하여 이미지 확보
driver.find_element_by_xpath(
    '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
selenium_scroll_option()

# 이미지 저장 src 요소를 리스트업 해서 이미지 url 저장
image = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# 클래스 네임에서 공백은 . 을 찍어줌

print(image)
image_url = []
for i in image:
    if i.get_attribute("src") != None :
        image_url.append(i.get_attribute("src"))
    else :
        image_url.append(i.get_attribute("data-src"))

# 전체 이미지 개수
print(f"전체 다운로드한 이미지 개수 : {len(image_url)}")
image_url = pd.DataFrame(image_url)[0].unique()

# 해당하는 파일에 이미지 다운로드
os.makedirs(r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\result_file\fruit\Dragon_fruit", exist_ok=True)
Dragon_fruit = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/Dragon_fruit/"
if image_name == 'Dragon_fruit' :
    for t, url in enumerate(image_url, 0) :
        urlretrieve(url, Dragon_fruit + image_name + "_" + str(t) + ".png")

    # driver.close()

print("용과 완료")

c = "lychee"
image_name = "lychee"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.google.co.kr/imghp?hl=ko")
browser = driver.find_element_by_name('q')
browser.send_keys(c)
browser.send_keys(Keys.RETURN)

# //*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input
selenium_scroll_option()# 스크롤 하여 이미지 확보
driver.find_element_by_xpath(
    '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
selenium_scroll_option()

# 이미지 저장 src 요소를 리스트업 해서 이미지 url 저장
image = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# 클래스 네임에서 공백은 . 을 찍어줌

print(image)
image_url = []
for i in image:
    if i.get_attribute("src") != None :
        image_url.append(i.get_attribute("src"))
    else :
        image_url.append(i.get_attribute("data-src"))

# 전체 이미지 개수
print(f"전체 다운로드한 이미지 개수 : {len(image_url)}")
image_url = pd.DataFrame(image_url)[0].unique()

# 해당하는 파일에 이미지 다운로드
os.makedirs(r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\result_file\fruit\lychee", exist_ok=True)
lychee = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/lychee/"
if image_name == 'lychee' :
    for t, url in enumerate(image_url, 0) :
        urlretrieve(url, lychee + image_name + "_" + str(t) + ".png")

    driver.close()

print("리치 완료")

d = "durian"
image_name = "durian"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.google.co.kr/imghp?hl=ko")
browser = driver.find_element_by_name('q')
browser.send_keys(d)
browser.send_keys(Keys.RETURN)

# //*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input
selenium_scroll_option()# 스크롤 하여 이미지 확보
driver.find_element_by_xpath(
    '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
selenium_scroll_option()

# 이미지 저장 src 요소를 리스트업 해서 이미지 url 저장
image = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# 클래스 네임에서 공백은 . 을 찍어줌

print(image)
image_url = []
for i in image:
    if i.get_attribute("src") != None :
        image_url.append(i.get_attribute("src"))
    else :
        image_url.append(i.get_attribute("data-src"))

# 전체 이미지 개수
print(f"전체 다운로드한 이미지 개수 : {len(image_url)}")
image_url = pd.DataFrame(image_url)[0].unique()

# 해당하는 파일에 이미지 다운로드
os.makedirs(r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\result_file\fruit\durian", exist_ok=True)
durian = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/durian/"
if image_name == 'durian' :
    for t, url in enumerate(image_url, 0) :
        urlretrieve(url, durian + image_name + "_" + str(t) + ".png")

    driver.close()

print("두리안 완료")
