# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:37:47 2017

@author: aroux
"""
import cv2

def image_resizer(img, scale) :
    
    size_x = img.shape[0]
    size_y = img.shape[1]
    
    img_resized = cv2.resize(img, (int(size_y*scale), int(size_x*scale)), interpolation = cv2.INTER_AREA)
    
    
    cv2.imshow("img_resized", img_resized)
    cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
    cv2.destroyAllWindows() #on ferme tout

    return(img_resized)
    
#    
#img1 = cv2.imread('photo1.JPG', 0) #image noir et blanc de la pièce
#
#cv2.imshow("img1", img1)
#cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
#cv2.destroyAllWindows() #on ferme tout
#
#im1 = image_resizer(img1, 0.1)
