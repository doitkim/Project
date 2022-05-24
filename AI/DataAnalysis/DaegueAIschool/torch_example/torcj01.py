import torch
import torchvision
import cv2
import numpy as np
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import time

#custom dataset

class TorchvisionDataset(Dataset):
    def __init__(self, file_path, labels, transfrom=None):
        self.file_path = file_path
        self.labels = labels
        self.transfrom = transfrom
    
    def __getitem__(self, index):
        label = self.labels[index]
        file_path = self.file_path[index]
        
        #Image open
        image = Image.open(file_path)
        
        start_t = time.time()
        if self.transfrom:
            image = self.transfrom(image)
        
        total_time = (time.time() - start_t)
        return image, label, total_time
    
    def __len__(self):
        return len(self.file)