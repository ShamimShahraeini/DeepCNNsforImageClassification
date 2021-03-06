import pickle
import pandas as pd
import matplotlib.pyplot as plt

# read python dict back from the file
# file = 'my_model_history_1'
file = 'my_simple_model_history'
# file = 'my_model_lite_history_1'
# file = 'my_model_lite_history_2'

pkl_file = open(file + '.pkl', 'rb')
model_history = pickle.load(pkl_file)
pkl_file.close()

# print(model_history)

loss_history_df = pd.DataFrame({'loss': model_history['loss'], 'val_loss': model_history['val_loss']})
loss_history_fig = loss_history_df.plot().get_figure()
loss_history_fig.savefig(file + '_loss_history_fig.png')

accuracy_history_df = pd.DataFrame({'accuracy': model_history['accuracy'], 'val_accuracy': model_history['val_accuracy']})
accuracy_history_fig = accuracy_history_df.plot().get_figure()
accuracy_history_fig.savefig(file + '_accuracy_history_fig.png')

plt.show()
