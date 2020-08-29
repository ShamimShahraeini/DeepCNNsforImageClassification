from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.applications import InceptionV3, InceptionResNetV2, ResNet152V2

def create_classification_model():

    # THESE LINES CREATE AND LOAD PRETRAINED WEIGHTS
    inception_model = InceptionV3(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    inception_model.summary()

    inception_resnet_model = InceptionResNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    inception_model.summary()

    resnet_model = ResNet152V2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    inception_model.summary()


    # IN HERE WE SHOULD PRE
    for layer in inception_model.layers:
        layer.trainable = False

    for layer in incepinception_resnet_modeltion_model.layers:
        layer.trainable = False

    for layer in resnet_model.layers:
        layer.trainable = False

    # Model Output Size = 7 x 7 x features

    inception_model_features = GlobalAveragePooling2D()(inception_model.output)
    inception_resnet_model_features = GlobalAveragePooling2D()(inception_resnet_model.output)
    resnet_model_features = GlobalAveragePooling2D()(resnet_model.output)

    # GAP Output Size = features

    feature_concatenation = Concatenate([inception_model_features, inception_resnet_model_features, resnet_model_features], axis=-1)

    x = Dense(1024, activation='relu')(feature_concatenation)

    prediction = Dense(20, activation='softmax')(x)

    my_model = Model(input, prediction)
    my_model.summary()

    return my_model




