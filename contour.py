# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:39:04 2017

@author: boetto
"""

import cv2
import numpy as np

import gradient as grd

img = cv2.imread('pièce.jpeg', 0) #image noir et blanc de la pièce

length = len(img[1])
height = len(img)

seuil_bas = 0
seuil_haut = 50

mat_cont = np.zeros((height,length))

for i in range (1, height):
    for j in range (1, length):
        if ((grd.grad_hor(img,i,j)<seuil_bas) or (grd.grad_vert(img,i,j)<seuil_bas)):
            mat_cont [i,j] = 255
        elif ((grd.grad_hor(img,i,j)>seuil_haut) or (grd.grad_vert(img,i,j)>seuil_haut)):
            mat_cont [i,j] = 0
        else :
            mat_cont [i,j] = 150

cv2.imshow('pièce', mat_cont)
cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
cv2.destroyAllWindows() #on ferme tout