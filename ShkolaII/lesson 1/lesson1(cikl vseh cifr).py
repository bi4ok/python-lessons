from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
from google.colab import files
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import toimage
%matplotlib inline
(x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data()
n = 1304
x_train = x_train_org.reshape(60000, 784)
x_test = x_test_org.reshape(10000, 784)
x_train = x_train.astype('float32')
x_train = x_train / 255
y_train = utils.to_categorical(y_train_org, 10)

def modeltest(sloi,neironi)
    model = Sequential()
    n = [neironi]
    for j in range(sloi):
        model.add(Dense(n[j], input_dim=784, activation="relu"))
    model.add(Dense(10, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(x_train, y_train, batch_size=200, epochs=20, verbose=1)


def acctest():
    n = 0
    for i in range(10000):
        plt.imshow(toimage(x_test_org[i]).convert('RGBA'))
        xt = x_test[i]
        xt = np.expand_dims(xt, axis=0)
        prediction = np.argmax(model.predict(xt))
        if prediction == y_test_org[i]:
            n += 1
    acc = n/10000
    print(acc)