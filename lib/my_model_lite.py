
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input, concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.applications import MobileNet, MobileNetV2, NASNetMobile
import numpy as np


def create_classification_model():

    input_layer = Input(shape=(224, 224, 3))

    # THESE LINES CREATE AND LOAD PRE-TRAINED WEIGHTS
    mobilenet_model = MobileNet(input_shape=(224, 224, 3), input_tensor=input_layer,
                                  include_top=False, weights='imagenet')
    # mobilenet_model.summary()

    mobilenet_v2_model = MobileNetV2(input_shape=(224, 224, 3), input_tensor=input_layer,
                                               include_top=False, weights='imagenet')
    # mobilenet_v2_model.summary()

    nasnet_mobile_model = NASNetMobile(input_shape=(224, 224, 3), input_tensor=input_layer, include_top=False, weights='imagenet')
    # nasnet_mobile_model.summary()

    # IN HERE WE SHOULD DEACTIVATE ALL THE LAYERS FOR LEARNING
    for layer in mobilenet_model.layers[:-6]:
        layer.trainable = False

    for layer in mobilenet_v2_model.layers[:-11]:
        layer.trainable = False

    for layer in nasnet_mobile_model.layers[:-36]:
        layer.trainable = False

    # inception_model.input = input_layer
    # inception_resnet_model.input = input_layer
    # resnet_model.input = input_layer

    # Model Output Size = 7 x 7 x features

    inception_model_features = GlobalAveragePooling2D()(mobilenet_model.output)
    inception_resnet_model_features = GlobalAveragePooling2D()(mobilenet_v2_model.output)
    resnet_model_features = GlobalAveragePooling2D()(nasnet_mobile_model.output)

    # GAP Output Size = features
    print(np.shape(inception_model_features))
    print(np.shape(inception_resnet_model_features))
    print(np.shape(resnet_model_features))

    feature_concatenation = concatenate([inception_model_features,
                                         inception_resnet_model_features,
                                         resnet_model_features],
                                        axis=-1)

    x = Dense(256, activation='relu')(feature_concatenation)
    x = Dropout(0.5)(x)

    prediction = Dense(4, activation='softmax')(x)

    my_model = Model(input_layer, prediction)
    my_model.summary()

    return my_model


# create_classification_model()





