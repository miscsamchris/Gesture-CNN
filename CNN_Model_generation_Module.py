# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:50:19 2019

@author: TLSWM
"""

from keras.models import Sequential
from keras.layers import Conv2D,Dropout
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Softmax
number=int(input())
classifier = Sequential()
classifier.add(Conv2D(64, (3, 3), input_shape = (128,128, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (4, 4)))
classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (4, 4)))
classifier.add(Flatten())
classifier.add(Dense(units = 1024, activation = 'relu'))
classifier.add(Dense(units = number,
                     kernel_initializer = 'uniform',
                     #Add the number of signs you wanna add +1
                     activation ="softmax" ))
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True)
training_set = train_datagen.flow_from_directory(directory='../Imageprocessing/Train/',target_size = (128, 128),batch_size = 32)
classifier.fit_generator(training_set,steps_per_epoch = 4000,epochs = 1,validation_steps = 2000)
classifier.save("GestureClassifier.h5")