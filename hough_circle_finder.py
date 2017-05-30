# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:34:09 2017

@author: aroux
"""

import cv2
import numpy as np

def circle_finder(img):
    """ prend en arg l'image lissee avec les bords detectes et retourne les cercles trouves """
    
    img = np.uint8(img) #necessaire pour que CV_HOUGH_GRADIENT fonctionne  
    #il faut aussi que l'image soit en nuances de gris
    
    min_dimension = min(img.shape)
    print(min_dimension)
    
    circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 40, param1=200, param2=100, minRadius=120, maxRadius = 160)
    #circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)

    #circles = np.uint8(np.around(circles))
    # les elements de circles sont de la forme [xCentre, yCentre, rayon]
    return circles


""" script de test"""
    
#img = cv2.imread('pièce.jpeg', 0) #image noir et blanc de la pièce
#img = cv2.medianBlur(img,5)
#circles = hough_circle_finder(img)
#
#for i in circles[0,:]:
#    # draw the outer circle
#    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
#    # draw the center of the circle
#    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
#    
#    
#    
#cv2.imshow('detected circles',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()