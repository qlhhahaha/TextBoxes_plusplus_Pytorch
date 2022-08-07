import os
import cv2
import shutil

src = 'D:/lab_working/SSD/TextBoxes_plusplus_Pytorch/icpr_mtwi_task2/output/output'

oldname = []
newname = []

for root, dirs, files in os.walk(src):
    for i, file in enumerate(files):
        oldname.append(os.path.join(root, file))
        file = file.replace('output', '')
        newname.append(os.path.join(root, file))
        os.rename(oldname[i], newname[i])
