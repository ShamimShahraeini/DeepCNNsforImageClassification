from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input, concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.applications import InceptionV3, InceptionResNetV2, ResNet152V2
import numpy as np


def create_classification_model():

    input_layer = Input(shape=(224, 224, 3))

    # THESE LINES CREATE AND LOAD PRE-TRAINED WEIGHTS
    inception_model = InceptionV3(input_shape=(224, 224, 3), input_tensor=input_layer,
                                  include_top=False, weights='imagenet')
    # inception_model.summary()

    inception_resnet_model = InceptionResNetV2(input_shape=(224, 224, 3), input_tensor=input_layer,
                                               include_top=False, weights='imagenet')
    # inception_resnet_model.summary()

    resnet_model = ResNet152V2(input_shape=(224, 224, 3), input_tensor=input_layer,
                               include_top=False, weights='imagenet')
    # resnet_model.summary()

    # IN HERE WE SHOULD DEACTIVATE ALL THE LAYERS FOR LEARNING
    for layer in inception_model.layers[:-22]:
        layer.trainable = False

    for layer in inception_resnet_model.layers[:-21]:
        layer.trainable = False

    for layer in resnet_model.layers[:-36]:
        layer.trainable = False

    # inception_model.input = input_layer
    # inception_resnet_model.input = input_layer
    # resnet_model.input = input_layer

    # Model Output Size = 7 x 7 x features

    inception_model_features = GlobalAveragePooling2D()(inception_model.output)
    inception_resnet_model_features = GlobalAveragePooling2D()(inception_resnet_model.output)
    resnet_model_features = GlobalAveragePooling2D()(resnet_model.output)

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


create_classification_model()




