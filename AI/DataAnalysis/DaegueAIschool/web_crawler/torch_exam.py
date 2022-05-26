from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
from urllib.request import (urlopen, urlparse, urlretrieve)
import torch
import torchvision
import cv2
import numpy as np
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
from matplotlib import pyplot as plt

# 구글 이미지 URL
chrome_path = "/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/driver/chromedriver"
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

a = "아이유"
image_name = "IU"
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
os.makedirs("/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/src/result_file/Image_Control/IU", exist_ok=True)
IU = "/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/src/result_file/Image_Control/IU/"
if image_name == 'IU' :
    for t, url in enumerate(image_url, 0) :
        urlretrieve(url, IU + image_name + "_" + str(t) + ".png")

    # driver.close()

print("아이유 완료")

# custom dataset

class TorchvisionDataset(Dataset):

    def __init__(self, file_paths, transform=None):
        self.file_paths = file_paths
        self.transform = transform

    def __getitem__(self, index):
        file_path = self.file_paths[index]

        # Image open
        image = Image.open(file_path)

        start_t = time.time()
        if self.transform:
            image = self.transform(image)
            total_time = (time.time() - start_t)
        return image, total_time

        def __len__(self):
            return len(self.file_path)

torchvision_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.RandomCrop((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])

route = "/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/src/result_file/Image_Control/IU/"
route1= "/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/src/result_file/Image_Control/"
torchvision_dataset = TorchvisionDataset(
    file_paths=[f"{route}IU_{i}.png" for i in range(0, len(os.listdir(f'{route}')))],
    transform=torchvision_transform
)
# print(os.listdir(f"{route}"))
os.makedirs(f"{route1}AUG_IU/", exist_ok=True)
total_time = 0
for i in range(0, len(os.listdir(f"{route}"))):
    sample, transform_time = torchvision_dataset[i]
    img = transforms.ToPILImage()(sample)
    img.save(f'{route1}AUG_IU/AUG_IU_{i}.png', 'png')
    total_time += transform_time

print("torchvision time / sample : {} ms ".format(total_time * 10))