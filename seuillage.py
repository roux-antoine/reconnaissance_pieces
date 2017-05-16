# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:41:14 2017

@author: aroux
"""

#script/fonction qui prend en a arg une image et la renvoit lissee

import cv2
import numpy as np

img = cv2.imread('pièce.jpeg',0) #image noir et blanc de la pièce

print(img)

img_blurred = cv2.GaussianBlur(img,(5,5), 0)

print(img_blurred)

cv2.imshow('img_blurred', img_blurred)
cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir