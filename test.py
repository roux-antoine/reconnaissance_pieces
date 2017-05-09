# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:56:42 2017

@author: boetto
"""

import cv2
import numpy as np

import gradient as grd

img = cv2.imread('pièce.jpeg', 0) #image noir et blanc de la pièce

length = len(img[1])
height = len(img)

print(img)
cv2.imshow('pièce', img)
cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
cv2.destroyAllWindows() #on ferme tout

Mat_grad = []

for i in range (1, height):
    for j in range (1, length):
        Mat_grad[i][j] = [grd.grad_hor(img,i,j),grd.grad_vert(img,i,j)]

#print(Mat_grad)