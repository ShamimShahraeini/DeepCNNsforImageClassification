
import cv2
import os
import random
import numpy as np


class DataGenerator:

    def __init__(self, prefix_address, neural_network_input_size=(224, 224)):
        self.prefix_address = prefix_address
        self.neural_network_input_size = neural_network_input_size

    def get_all_data(self):

        images = []
        labels = []

        list_files = os.listdir(self.prefix_address)
        random.seed(101)
        random.shuffle(list_files)

        for file in list_files:

            # print(file)
            image = cv2.imread(os.path.join(self.prefix_address, file))
            # cv2.imshow('test', image)
            # cv2.waitKey(0)
            resized_image = cv2.resize(image, self.neural_network_input_size).astype('float') / 255.0
            images.append(resized_image)

            if 'cloudy' in file:
                labels.append([1, 0, 0, 0])

            if 'rain' in file:
                labels.append([0, 1, 0, 0])

            if 'shine' in file:
                labels.append([0, 0, 1, 0])

            if 'sunrise' in file:
                labels.append([0, 0, 0, 1])

        print(np.shape(images))
        print(np.shape(labels))

        # TRAIN TEST SPLIT
        split_index = int(0.8 * len(images))
        x_train = np.array(images[:split_index])
        y_train = np.array(labels[:split_index])

        x_test = np.array(images[split_index:])
        y_test = np.array(labels[split_index:])

        return x_train, y_train, x_test, y_test


# data_generator = DataGenerator('dataset2/', (224, 224))
#
# x_train, y_train, x_test, y_test = data_generator.get_all_data()




