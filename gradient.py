# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:49:14 2017

@author: boetto
"""

import numpy as np

def grad_hor(img,x,y):
    return img[x][y]-img[x-1][y]

def grad_vert(img,x,y):
    return img[x][y]-img[x][y-1]

def angle_grad(img, x,y):
    return np.atan(grad_vert(img,x,y)/grad_hor(img,x,y))

def force_grad(img,x,y):
    return np.sqrt(grad_vert(img,x,y)**2 + grad_hor(img,x,y)**2)

