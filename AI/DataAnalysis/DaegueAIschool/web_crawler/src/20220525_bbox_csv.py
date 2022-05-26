import os
import json
import cv2
import csv

json_path = r"D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\exam_dataset_220525\anno\raccoon_annotations.coco.json"

# 파일 읽어오기
with open(json_path, "r") as f:
    coco_info = json.load(f)

assert len(coco_info) > 0, "파일 읽기 실패"

# 카테고리 정보 수집
categories = dict()
for category in coco_info['categories']:
    categories[category['id']] = category['name']

# annotaion 정보
annotation_info = dict()
name = []
# name_s = []
# name_ss = []

csvfile = open(fr'D:\study\DaeguAI\Project\AI\DataAnalysis\DaegueAIschool\web_crawler\src\exam_dataset_220525\result_2\raccoon.csv',"w",newline="")
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['file_name', 'x', 'y', 'w', 'h'])

for i in range(0, len(coco_info['images'])):
    # file_name = coco_info['images'][i]['file_name']
    name.append(coco_info['images'][i]['file_name'])
    for i in range(0, len(name)):
        bbox = coco_info['annotations'][i]['bbox']
    # name_s.append(name[i].split('.'))
    # name_ss.append(name_s[i][0].replace('_', '.'))
    csvwriter.writerow([name[i], bbox[0], bbox[1], bbox[2], bbox[3]])
    # csvwriter.writerow([name_ss[i], bbox[0], bbox[1], bbox[2], bbox[3]])

csvfile.close()
