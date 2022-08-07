import os
import cv2
import shutil

txtName = 'D:/lab_working/SSD/TextBoxes_plusplus_Pytorch/mtwi_2018_train/txt_train'
imgName = 'D:/lab_working/SSD/TextBoxes_plusplus_Pytorch/mtwi_2018_train/image_train'
new_path = 'D:/lab_working/SSD/TextBoxes_plusplus_Pytorch/mtwi_2018_train/new_txt_train'

txt_path = []
image_path = []
all_path = []

for root, dirs, files in os.walk(txtName):
    for file in files:
        all_path.append(os.path.join(root, file))
        file = file.replace('.txt', '.jpg')
        file = file.replace('.jpg', '')
        txt_path.append( file)

txt_path.sort()
all_path.sort()

for root, dirs, files in os.walk(imgName):
    for file in files:
        file = file.replace('.jpg', '')
        image_path.append( file)
image_path.sort()


for i,file in enumerate(txt_path):
    if file not in image_path:
        shutil.move(all_path[i], new_path)