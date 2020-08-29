#
from my_simple_model import create_classification_model
from tensorflow.keras.models import save_model
import numpy as np
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd
from matplotlib import pyplot
from tensorflow.keras.datasets import cifar10

# LOAD CIFAR DATASET
# X_train Y_train, X_test, Y_test
(X_train, Y_train), (X_test, Y_test) = cifar10.load_data()
# summarize loaded dataset
print('Train: X=%s, y=%s' % (X_train.shape, Y_train.shape))
print('Test: X=%s, y=%s' % (X_test.shape, Y_test.shape))
# plot first few images
# for i in range(9):
# 	# define subplot
# 	pyplot.subplot(330 + 1 + i)
# 	# plot raw pixel data
# 	pyplot.imshow(X_train[i])
# # show the figure
# pyplot.show()
# CREATING OUR MODEL
my_model = create_classification_model()

my_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# EARLY STOPPING


# TRAINING THE MODEL
my_model.fit(X_train, Y_train, batch_size=32, epochs=100, validation_data=(X_test, Y_test))

model_history = my_model.history.history

# IF YOU WANNA SAVE MODEL OR MODEL WEIGHTS
save_model(my_model, 'model_checkpoint.h5')
my_model.save_weights('model_checkpoint_weights.h5')

history_df = pd.DataFrame(model_history)
history_df.plot()

# NOW WE CAN USE OUR MODEL TO PREDICT A TEST IMAGE
image_class = my_model.predict(X_test[0])
class_number = np.argmax(image_class)








