# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:41:14 2017

@author: aroux
"""



import cv2

def blur_image(img,kernel_size) : 
    """fonction qui prend en arg une image et la renvoie floutee"""

    #kernel_size = 7
    #ATTENTION : kernel_size doit etre un nbr impair 
    img_blurred = cv2.GaussianBlur(img,(kernel_size,kernel_size), 0)
    
    return img_blurred

    #cv2.imshow('img_blurred', img_blurred)
    #cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
    
    
