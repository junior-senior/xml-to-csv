import pandas as pd
import numpy as np
import os
import glob
#import keras
import matplotlib.pyplot as plt
import xml.etree.ElementTree as e_tree
from collections import Counter
import csv

folder_path = ''

#collated_label_file_path = 'Training Images/labels/'

class_list = []


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


f = open("%FILENAME%.csv", 'w')
f.write("image_name, image_width, image_height, image_depth, class, XMin, XMax, YMin, YMax" + '\n')
csv = ''
for folder in os.listdir(folder_path):
    for file in os.listdir(folder_path + folder):
        if file.endswith(".xml"):
            #print(folder)
            jpg_file, extension = file.split('.')
            jpg_file = jpg_file + '.jpg'
            root = e_tree.parse(folder_path + folder + '/' + file).getroot()
            csv = '{name}, {width}, {height}, {depth}, {object}, {xmin}, {xmax}, {ymin}, {ymax}'.format(
                name=jpg_file, width=root[0][0].text, height=root[0][1].text, depth=root[0][2].text, object=root[1][0].text,
                xmin=root[1][1][0].text, ymin=root[1][1][1].text, xmax=root[1][1][2].text, ymax=root[1][1][3].text)
            print(csv)
            f.write(csv + '\n')

print((pd.read_csv("%FILENAME%.csv")))
