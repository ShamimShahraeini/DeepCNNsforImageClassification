import os
import cv2
import numpy as np
import pandas as pd

# Read All the Files

dataset_files = os.listdir('dataset2')

# start
X_train = []
Y_train = []
lst = []

for file in dataset_files:

    # Load the image.
    # print(file)
    dataset_img = cv2.imread('dataset2/' + file)
    img_object = dataset_img
    # print(type(img_object))
    # cv2.imshow("dataset", img_object)
    # cv2.waitKey(0)
    resized_image = cv2.resize(img_object, (224, 224)).astype('float') / 255.0
    # cv2.imshow("dataset", resized_image)
    # cv2.waitKey(0)
    X_train.append(resized_image)
    if 'cloudy' in file.split('.')[-2]:
        lst.append('cloudy')
    elif 'rain' in file.split('.')[-2]:
        lst.append('rain')
    elif 'shine' in file.split('.')[-2]:
        lst.append('shine')
    elif 'sunrise' in file.split('.')[-2]:
        lst.append('sunrise')


df = pd.DataFrame({'type': lst})
# print(df)
# df.to_csv('my_dataset_csv.csv')
dummies = pd.get_dummies(df.type)
dummies.to_csv('my_dataset_csv.csv')

