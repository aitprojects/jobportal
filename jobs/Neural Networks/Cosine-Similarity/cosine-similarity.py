# -*- coding: utf-8 -*-

import keras
from keras.layers import Input, Dense
from keras.models import Model
import numpy as np


def computeMeanConsineAngle(x,y):
    cosMean = 0
    numSample = x.shape[0]
    for i in range(numSample):
        cosMean += np.dot(x[i,:],y[i,:])/np.sqrt(np.dot(x[i,:],x[i,:])*np.dot(y[i,:],y[i,:]))
        
    return cosMean/float(numSample)

X = np.random.random((1000,3))
Y = X

inputs = Input(shape=(3,))
preds = Dense(3,activation='linear')(inputs)
model = Model(inputs=inputs,outputs=preds)

sgd=keras.optimizers.Adam(lr=1e-2)
model.compile(optimizer=sgd ,loss='mse',metrics=['cosine_proximity'])
model.fit(X,Y, batch_size=1000, epochs=500, shuffle=False)

pred = model.predict(X)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(X, pred)



plt.scatter(pred,Y)

print('mse = ', mse)
print(computeMeanConsineAngle(pred, Y))

testX = np.array([[1,0]])
testY = np.array([[1,0]])
computeMeanConsineAngle(testX,testY)