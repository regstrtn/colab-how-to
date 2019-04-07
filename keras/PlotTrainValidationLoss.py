import keras
from keras import layers
from keras.models import Sequential

input_dim = x_train.shape[1] #Number of features in x_train
model = Sequential()
model.add(layers.Dense(3, input_dim = input_dim, activation= 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', 
             optimizer = 'adam',
              metrics = ['mae', 'accuracy']
             )
model.summary()

#History will now store values of train acc, validation acc, train loss, validation loss
history = model.fit(x_train, y_train,
                   epochs = 10,
                   verbose = True,
                   validation_data = (x_test, y_test),
                   batch_size = 10
                   )

import matplotlib.pyplot as plt
plt.style.use('ggplot')

def plot_history(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
