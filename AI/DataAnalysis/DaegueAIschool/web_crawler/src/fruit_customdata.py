import os
# from h11 import Data
import torch
import glob
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.data import Dataset

class MyCustomDataset(Dataset):

    def __init__(self, path):
       self.all_data = sorted(glob.glob(os.path.join(path, '*','*.png')))

    def __getitem__(self, index):
        data_path = self.all_data[index]
        data_split = data_path.split('\\')
        data_labels = data_split[1]

        labels = 0
        if data_labels == 'mango':
            labels = 0
        elif data_labels == 'lychee':
            labels = 1
        elif data_labels == 'durian':
            labels = 2
        elif data_labels == 'Dragon_fruit':
            labels = 3

        return data_path, labels

    def __len__(self):
        # 전체 길이를 반환 -> 리스트 [] len()
        return len(self.all_data)

# 2가지 구성 필요 -> dataset dataloader
dataset = MyCustomDataset(path="D:/study/DaeguAI/Project/AI/DataAnalysis/DaegueAIschool/web_crawler/src/result_file/fruit/")
dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
for path, label in dataloader:
    print(path, label)
