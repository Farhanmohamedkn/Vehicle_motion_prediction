import matplotlib.pyplot as plt
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras import layers
from keras import activations
import numpy as np
from keras.optimizers import SGD


def FCN_keras_model(xTrain, xTest, yTrain, yTest):
    # flatten the input and output
    n_input = np.shape(xTrain)[1] * np.shape(xTrain)[2]
    xTrain = np.reshape(xTrain, (np.shape(xTrain)[0], n_input))
    n_output = np.shape(yTrain)[1] * np.shape(yTrain)[2]
    yTrain = np.reshape(yTrain, (np.shape(yTrain)[0], n_output))

    xTest = np.reshape(xTest, (np.shape(xTest)[0], n_input))
    yTest = np.reshape(yTest, (np.shape(yTest)[0], n_output))

    # define multi-layer perceptron model
    model = Sequential()
    model.add(Dense(500, activation='relu', input_shape=(n_input,)))
    #model.add(Dropout(0.5))
    model.add(Dense(250, activation='relu'))
    #model.add(Dropout(0.5))
    model.add(Dense(100, activation='relu'))
    #model.add(Dropout(0.5))
    model.add(Dense(50, activation='relu'))
    #model.add(Dropout(0.5))
    model.add(Dense(25, activation='softmax'))
    model.add(Dense(n_output))
    sgd=SGD(learning_rate=0.01, momentum=0.0, nesterov=True)
    model.compile(optimizer=sgd, loss='mse')

    # fit the keras model on the dataset
    history =model.fit(xTrain, yTrain, epochs=100, verbose=1, validation_data=(xTest, yTest))

    # save the trained model
    filepath = 'FCN_model.h5'
    model.save(filepath)

    # load trained model
    model = keras.models.load_model('FCN_model.h5')

    # Training and validation loss plot
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model train vs validation loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper right')

    return model