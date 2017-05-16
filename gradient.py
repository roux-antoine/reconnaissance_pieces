# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:49:14 2017

@author: boetto
"""

import numpy as np

eps = 0.01

def grad_hor(img,x,y):
    return img[x][y]-img[x-1][y]

def grad_vert(img,x,y):
    return img[x][y]-img[x][y-1]

def angle_grad(img, x,y):
    if (grad_hor(img,x,y)<eps or -eps<grad_hor(img,x,y)):
        return (grad_hor(img,x,y)*90) #ATTENTION ÇA PEUT AUSSI ETRE -90
    
    else:
        return (np.arctan(grad_vert(img,x,y)/grad_hor(img,x,y)))*180/np.pi

def force_grad(img,x,y):
    return np.sqrt(grad_vert(img,x,y)**2 + grad_hor(img,x,y)**2)

def mat_grad(img):
    mat_grad = np.zeros((len(img),len(img[1])))
    for i in range(1,len(img)):
        for j in range(1,len(img[1])):
            mat_grad[i,j] = force_grad(img,i,j)
    print(mat_grad)
