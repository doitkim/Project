import os
import json
import PIL.ImageOps
import cv2
from PIL import Image
from PIL import ImageOps
idx = 0

json_path = "/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/src/exam_dataset_220525/anno/raccoon_annotations.coco.json"

# 파일 읽어오기
with open(json_path, "r") as f:
    coco_info = json.load(f)

assert len(coco_info) > 0, "파일 읽기 실패"

# print(coco_info)

# 카테고리 정보 수집
categories = dict()
for category in coco_info['categories']:
    categories[category["id"]] = category["name"]
    # print(categories)

# annotaiton 정보
ann_info = dict()
for annotation in coco_info['annotations']:
    # print("annotation >> ", annotation)
    image_id = annotation["image_id"]
    bbox = annotation["bbox"]
    category_id = annotation["category_id"]
    # print(image_id,bbox,category_id)
    if image_id not in ann_info:
        ann_info[image_id] = {
            "boxes": [bbox], "categories": [category_id]
        }
    else:
        ann_info[image_id]["boxes"].append(bbox)
        ann_info[image_id]["categories"].append(categories[category_id])

for image_info in coco_info['images']:
    filename = image_info["file_name"]
    height = image_info["height"]
    width = image_info["width"]
    img_id = image_info["id"]

    file_path = os.path.join("/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/src/exam_dataset_220525/data/", filename)
    # ./0525_image_data/image.jpeg
    # image read
    img = cv2.imread(file_path)

    try:
        annotation = ann_info[img_id]
    except KeyError:
        continue

    print(annotation)
    for bbox, category in zip(annotation["boxes"], annotation["categories"]):
        x1, y1, w, h = bbox

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2

        org_img = img.copy()
        crop_img = org_img[ int(x1):int(x1 + w),int(y1):int(y1 + h)]
        cv2.imshow("test", crop_img)
        cv2.waitKey(500)
        if (h > w):
            h1 = 255
            w1 = 255 / int(h) * int(w)
            print("h1 :",h1)
            print("w1 :", w1)

        else:
            h1 = 255 / int(w) * int(h)
            w1 = 255
            print("h1 :", h1)
            print("w1 :", w1)

        resize_img = cv2.resize(crop_img, (int(w1), int(h1)))

        w2 = 255 - int(w1)
        h2 = 255 - int(h1)
        top, bottom = h2 // 2, h2 - (h2 // 2)
        left, right = w2 // 2, w2 - (w2 // 2)

        padding_img = cv2.copyMakeBorder(resize_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        cv2.imwrite("/home/leesera/PycharmProjects/DaeguAI/venv/Web_crawler/src/exam_dataset_220525/result_1/" + "raccoon_Padding" + str(idx) + ".png", padding_img)
        print(idx, "번 파일 저장")
        idx += 1
        # print("org_img >>",org_img)
        # if category == 1 :
        #     category = "ros"
        #
        # text_img = cv2.putText(img, str(category),(int(x1), int(y1)-10), font, fontScale, color, thickness, cv2.LINE_AA)
        # rec_img = cv2.rectangle(text_img, (int(x1), int(y1)), (int(x1+w), int(y1+h)), (255, 0, 255), 2)
        # cv2.imshow("test", rec_img)
