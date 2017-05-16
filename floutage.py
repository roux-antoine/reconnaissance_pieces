# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:41:14 2017

@author: aroux
"""

#script qui prend en arg une image et la renvoie floutee

import cv2

img = cv2.imread('pièce.jpeg',0) #image noir et blanc de la pièce

kernel_size = 7
#ATTENTION : kernel_size doit etre un nbr impair 

img_blurred = cv2.GaussianBlur(img,(kernel_size,kernel_size), 0)

cv2.imshow('img_blurred', img_blurred)
cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir