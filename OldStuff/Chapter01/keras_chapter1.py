import keras as keras
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np
np.random.seed(9)

#it seems the model is our actual neural network, a sequential model is a typical feedforward model, and we can choose the activation, number of layers, and number of neurons (units per model)
model = Sequential()

#z=keras.Input((3,))
# Layer 1
model.add(Dense(units=4, activation='sigmoid', input_dim=3))
# Output Layer
model.add(Dense(units=1, activation='sigmoid'))

sgd = optimizers.SGD(learning_rate=1.0)
model.compile(loss='mean_squared_error', optimizer=sgd)

"""Here, we are essentially telling the computer that given an input array of X, it should give us an output array of y. So it's initially going to guess return arrays, but the cost function gradually brings it closer to y."""
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
y = np.array([[1],[1],[1],[0]])

#X is input, y is correct output
model.fit(X, y, epochs=1500, verbose=False)

print(model.predict(X))
