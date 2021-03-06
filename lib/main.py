#
from my_simple_model import create_classification_model
from data_generator import DataGenerator
from tensorflow.keras.models import save_model
import numpy as np
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd

# LOAD ALL THE DATA
data_generator = DataGenerator('dataset2/', (224, 224))
x_train, y_train, x_test, y_test = data_generator.get_all_data()
print(np.shape(x_train))
print(np.shape(y_train))
print(np.shape(x_test))
print(np.shape(y_test))

# CREATING OUR MODEL
my_model = create_classification_model()

# COMPILE THE MODEL
my_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# EARLY STOPPING
early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1)

# TRAINING THE MODEL
my_model.fit(x_train, y_train, batch_size=128, epochs=200, validation_data=(x_test, y_test))

model_history = my_model.history.history

# IF YOU WANNA SAVE MODEL OR MODEL WEIGHTS
save_model(my_model, 'model_early_stop.h5')
my_model.save_weights('model_checkpoint_weights.h5')

history_df = pd.DataFrame(model_history)
history_df.plot()

# NOW WE CAN USE OUR MODEL TO PREDICT A TEST IMAGE
image_class = my_model.predict(x_test[0])
class_number = np.argmax(image_class)








