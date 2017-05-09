# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:49:14 2017

@author: boetto
"""

def grad_hor(img,x,y):
    return img[x][y]-img[x-1][y]

def grad_vert(img,x,y):
    return img[x][y]-img[x][y-1]