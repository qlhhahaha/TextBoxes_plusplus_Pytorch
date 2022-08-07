import os.path as osp
import os
import torch
import torch.utils.data as data
import cv2
import numpy as np

import os.path as osp
import numpy as np

MTWI_CLASSES = (  # always index 0
    'text',)

root = r"D:\lab_working\SSD\TextBoxes_plusplus_Pytorch\mtwi_2018_train"
annopath = osp.join(root, 'txt_train', '{}.txt')
imgpath = osp.join(root, 'image_train', '{}.jpg')

def mtwiChecker(image_id, width, height):
    with open(annopath.format(image_id), 'r', encoding='utf-8') as files:
        target = files.readlines()
    res = []

    for obj in target:
        obj_list = obj.strip().split(',')
        if obj_list[8] == '###':
            continue

        name = 'text'

        pts = ['xmin', 'ymin', 'xmax', 'ymax']
        bndbox = []

        for i, pt in enumerate(obj_list[:8]):
            cur_pt = float(pt)
            # scale height or width
            cur_pt = cur_pt / width if i % 2 == 0 else cur_pt / height
            bndbox.append(cur_pt)

        # print(name)
        p12 = (bndbox[0] - bndbox[2], bndbox[1] - bndbox[3])
        p23 = (bndbox[2] - bndbox[4], bndbox[3] - bndbox[5])
        if p12[0] * p23[1] - p12[1] * p23[0] < 0:
            bndbox[0:7:2] = bndbox[6::-2]
            bndbox[1:8:2] = bndbox[7::-2]
        label_idx = dict(zip(MTWI_CLASSES, range(len(MTWI_CLASSES))))[name]
        bndbox.append(label_idx)
        res += [bndbox]  # [x1, y1, x2, y2, x3, y3, x4, y4, label_ind]
        # img_id = target.find('filename').text[:-4]
    # print(res)

    try:
        print(np.array(res)[:, 8])
        print(np.array(res)[:, :8])
    except IndexError:
        print("\nINDEX ERROR HERE !", image_id)
        exit(0)
    return res  # [[xmin, ymin, xmax, ymax, label_ind], ... ]


if __name__ == '__main__':

    i = 0
    ids = list()

    for name in sorted(os.listdir(osp.join(root, 'txt_train'))):
        ids.append(name.replace('.txt', ''))
        # as we have only one annotations file per image
        img_id = ids[i]
        img = cv2.imread(imgpath.format(img_id))
        height, width, channels = img.shape
        #print("path : {}".format(annopath % (root, name.split('.')[0])))
        res = mtwiChecker(img_id, width, height)
        i += 1

    print("Total of annotations : {}".format(i))
