from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input
from tensorflow.keras.models import Model
from tensorflow.keras.applications import InceptionV3, InceptionResNetV2, ResNet152V2


def create_classification_model():

    # THESE LINES CREATE AND LOAD PRE-TRAINED WEIGHTS
    resnet_model = ResNet152V2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    resnet_model.summary()

    # IN HERE WE SHOULD DEACTIVATE ALL THE LAYERS FOR LEARNING
    for layer in resnet_model.layers[:-36]:
        layer.trainable = False

    # Model Output Size = 7 x 7 x features

    model_features = GlobalAveragePooling2D()(resnet_model.output)

    # GAP Output Size = features

    x = Dense(256, activation='relu')(model_features)
    x = Dropout(0.5)(x)

    prediction = Dense(4, activation='softmax')(x)

    my_model = Model(resnet_model.input, prediction)
    my_model.summary()

    return my_model


create_classification_model()

