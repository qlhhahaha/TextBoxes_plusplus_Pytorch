import os
import cv2
import shutil

dirName = 'D:/lab_working/SSD/TextBoxes_plusplus_Pytorch/icpr_mtwi_task2/image_test'
# 将dirName路径下的所有文件路径全部存入all_path列表
all_path = []
for root, dirs, files in os.walk(dirName):
    for file in files:
        if "jpg" in file:
            all_path.append(os.path.join(root, file))
all_path.sort()

bad = []
badpath = 'D:/lab_working/SSD/TextBoxes_plusplus_Pytorch/icpr_mtwi_task2/check'

for i in range(len(all_path)):
    org = all_path[i]
    # print(all_path[i].split('/')[-1])
    try:
        img = cv2.imread(org)
        ss = img.shape
    except:
        bad.append(all_path[i])
        shutil.move(all_path[i], badpath)

        continue

#os.remove(all_path[i])

print('共有%s张坏图' % (len(bad)))
print(bad)
print('=========DONE=========')