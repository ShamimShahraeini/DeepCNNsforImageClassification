from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.applications import InceptionV3, InceptionResNetV2, ResNet152V2

def create_classification_model():

    # THESE LINES CREATE AND LOAD PRETRAINED WEIGHTS
    inception_model = ResNet152V2(input_shape=(32, 32, 3), include_top=False, weights='imagenet')
    inception_model.summary()


    # IN HERE WE SHOULD PRE
    for layer in inception_model.layers:
        layer.trainable = False

    # Model Output Size = 7 x 7 x features

    inception_model_features = GlobalAveragePooling2D()(inception_model.output)

    # GAP Output Size = features

    x = Dense(128, activation='relu')(inception_model_features)

    prediction = Dense(20, activation='softmax')(x)

    my_model = Model(inception_model.input, prediction)
    my_model.summary()

    return my_model




