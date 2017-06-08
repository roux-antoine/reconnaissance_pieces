# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:15:54 2017

@author: aroux
"""

import gradient as grd

def line_width_reducer (mat_grad, mat_cont, img) : 
    """ prend en arg la matrice du gradient, la matrice des contours et l'image
        affine les lignes de la matrice des contours 
        retourne la matrice des contours avec les lignes d'epaisseur 1"""
        
    length = len(mat_grad[1])
    height = len(mat_grad)
    
    for i in range (1,height-1):
        for j in range (1,length-1):
            
            if (-22,5<=grd.angle_grad(img,i,j) and grd.angle_grad(img,i,j)<=22,5):
                
                if (mat_grad[i,j+1]>mat_grad[i,j] or mat_grad[i,j-1]>mat_grad[i,j]):
                    mat_cont[i,j] = 255
                    
            if (22,5<grd.angle_grad(img,i,j) and grd.angle_grad(img,i,j)<67,5 ):
                if (mat_grad[i-1,j+1]>mat_grad[i,j] or mat_grad[i+1,j-1]>mat_grad[i,j]):
                    mat_cont[i,j] = 255
                    
            if (grd.angle_grad(img,i,j)<=-67,5 or 67,5<=grd.angle_grad(img,i,j)):
                if (mat_grad[i-1,j]>mat_grad[i,j] or mat_grad[i+1,j]>mat_grad[i,j]):
                    mat_cont[i,j] = 255
                    
            if (-67,5<grd.angle_grad(img,i,j) and grd.angle_grad(img,i,j)<-22,5 ):
                if (mat_grad[i+1,j+1]>mat_grad[i,j] or mat_grad[i-1,j-1]>mat_grad[i,j]):
                    mat_cont[i,j] = 255
                    
    return mat_cont