# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:34:09 2017

@author: aroux
"""

import cv2
import numpy as np

def hough_circle_finder(img):
    """ prend en arg l'image lissee avec les bords detectes et retourne les cercles trouves """
    
    circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 50,
                            param1=50, param2=30, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))

    return circles


""" script de test"""
    
img = cv2.imread('pièce.jpeg', 0) #image noir et blanc de la pièce

circles = hough_circle_finder(img)

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    
    
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()