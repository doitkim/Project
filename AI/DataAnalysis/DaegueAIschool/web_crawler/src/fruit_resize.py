from PIL import Image
import os.path
# resize_dir = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/resize/"
# os.mkdir(resize_dir)

file_path = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/mango/"

file_name = os.listdir(file_path)

total_image_number = len(file_name)

for i in range(0, total_image_number):
    im = Image.open(file_path+file_name[i])
    print(im.resize((255,255)))
    im.save(f"{file_path}mango_resize_{i}.png", quality=100)
    # im.save(f"{resize_dir}mango_resize_{i}.png",quality=100)


file_path = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/Dragon_fruit/"

file_name = os.listdir(file_path)

total_image_number = len(file_name)

for i in range(0, total_image_number):
    im = Image.open(file_path+file_name[i])
    print(im.resize((255,255)))
    im.save(f"{file_path}Dragon_fruit_resize_{i}.png", quality=100)
    # im.save(f"{resize_dir}Dragon_fruit_resize_{i}.png",quality=100)

file_path = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/lychee/"

file_name = os.listdir(file_path)

total_image_number = len(file_name)

for i in range(0, total_image_number):
    im = Image.open(file_path+file_name[i])
    print(im.resize((255,255)))
    im.save(f"{file_path}lychee_resize_{i}.png", quality=100)
    # im.save(f"{resize_dir}lychee_resize_{i}.png",quality=100)

file_path = "D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/durian/"

file_name = os.listdir(file_path)

total_image_number = len(file_name)

for i in range(0, total_image_number):
    im = Image.open(file_path+file_name[i])
    print(im.resize((255,255)))
    im.save(f"{file_path}durian_resize_{i}.png", quality=100)
    # im.save(f"{resize_dir}durian_resize_{i}.png",quality=100) resize 파일 따로 저장 할 때 사용





