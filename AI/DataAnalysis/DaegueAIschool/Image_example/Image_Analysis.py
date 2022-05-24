from genericpath import exists
import random
import numpy as np
import os
import cv2
import glob
from PIL import Image
import PIL.ImageOps

#PIL -> pip install Pillow
#cv2 -> pip install opencv-python

#새로만들 이미지 갯수를 정합니다.
num_augmented_images=50

#원본 사진 폴더 경로
file_path = "C:/Users/user/Desktop/대구AI스쿨/Project/AI/DataAnalysis/DaegueAIschool/Image_example/Image_sample"

#위의 폴더 내부에 있는 이미지 이름의 배열이 저장 되는 형태
file_name = os.listdir(file_path)
print(file_name)

#['IU01.jpg', 'IU02.jpg', 'IU03.jpg']

# file_name 길이를 가져옴
total_origin_image_number = len(file_name)
print("total Image number >>",total_origin_image_number)

# total Image number >> 3

augment_cnt = 1

for i in range(1,num_augmented_images):
    chage_picture_index = random.randint(0,total_origin_image_number-1)
    # print(chage_picture_index)
    file_names = file_name[chage_picture_index]
    # print(file_names)
    
    os.makedirs("./custom_data", exist_ok=True)
    origin_image_path = "C:/Users/user/Desktop/대구AI스쿨/Project/AI/DataAnalysis/DaegueAIschool/Image_example/Image_sample/" + file_names
    print(origin_image_path)
    
    image = Image.open(origin_image_path)
    
    #랜덤 값이 1~4 사이의 값이 나오도록 만듦
    
    random_augment = random.randrange(1,7)
    print(random_augment)
    
    if(random_augment == 1):
        #이미지 좌우 반전
        inverted_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        inverted_image.save("./custom_data/" + "inverted_" + str(augment_cnt) + ".png")
        
    elif(random_augment == 2):
        # 이미지 기울기
        rotated_image = image.rotate(random.randrange(-20,20))
        rotated_image.save("./custom_data/" + "rotated_" + str(augment_cnt) + ".png")
        
    elif(random_augment == 3):
        
        # 이미지 리사이즈
        resize_image = image.resize(size=(224, 224))
        resize_image.save("./custom_data/" + "resize_" +str(augment_cnt) + ".png")
        
        # 3가지 추가 (상하, 컬러지티,그레이, 센터크롭,크롭,랜덤크롭 등 )
        
        # 이미지 상하반전
    elif(random_augment == 4):
        
        top_bottom_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        top_bottom_image.save("./custom_data/" + "top_bpttpm_" +str(augment_cnt) + ".png")
        
        # 제출 코드만
        
        
    augment_cnt += 1
