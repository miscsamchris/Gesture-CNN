# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:08:53 2019

@author: TLSWM
"""

import cv2
import numpy as np
import os
import sys
path="D:/Projects/Imageprocessing/Train/"
number=0
while True:
    Actionname=str(input())
    i=1
    flag=False
    number
    number+=1
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, img = cap.read()
        cv2.rectangle(img, (400,400), (100,100), (0,255,0),0)
        crop_img = img[100:400, 100:400]
        if i<1000 and flag:
            cv2.imwrite(path+Actionname+"/"+str(i)+".jpg",crop_img)
            cv2.putText(img,str(i), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            i+=1
        if 1==1000:
            cv2.wr
        cv2.imshow('Image Capture', crop_img)
        cv2.imshow('Complete', img)
        k = cv2.waitKey(10)
        if k == ord("p"):
            flag=True
        if k==ord("c"):
            os.mkdir(path+Actionname)
        if k==ord("n"):
            cap.release()
            cv2.destroyAllWindows()
            break
        if k==27:
            cap.release()
            cv2.destroyAllWindows()
            sys.exit(0)
