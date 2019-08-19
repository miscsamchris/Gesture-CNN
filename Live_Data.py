# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:37:36 2019

@author: TLSWM
"""
import cv2
import numpy as np
import os
import sys
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
from keras.preprocessing import image
cap = cv2.VideoCapture(0)
listofclasses=["gesture 1","gesture 2","gesture 3"]
classifier = load_model('GestureClassifier.h5')
while(cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img, (400,400), (100,100), (0,255,0),0)
    crop_img = img[100:400, 100:400]
    cv2.imwrite("test.jpg",crop_img)
    test_image = image.load_img('test.jpg', target_size = (128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    print(listofclasses[np.argmax(result)])
    cv2.imshow('Complete', img)
    k = cv2.waitKey(10)
    if k==27:
        cap.release()
        cv2.destroyAllWindows()
        sys.exit(0)