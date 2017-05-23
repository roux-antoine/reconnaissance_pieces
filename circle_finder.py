# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:36:08 2017

@author: boetto
"""
import numpy as np


def circle_finder(mat_cont):
    length = len(mat_cont[1])
    height = len(mat_cont)
    mat_centre = np.zeros((3,height,length))
    
    for r in range (0,3):    
        R = 100 + 10*r
        
        for i in range (0,height):
            for j in range (0,length):
                teta = 0
                if(mat_cont[i,j]==0): #je suis un point noir
                    
                    while (teta < 2*np.pi): #parcourt du paramètre teta de 0 à 2*pi
                    
                        if(0<=i+R*np.cos(teta)<height and 0<=j+R*np.sin(teta)<length): #on vérifie qu'on est dans la matrice
                        
                            if(int(R*np.cos(teta))!= int(R*np.cos(teta)) or int(R*np.sin(teta))!= int(R*np.sin(teta-180/np.pi))): #on s'assure de ne pas incrémenter deux fois le même "centre"
                                mat_centre[r,i+int(R*np.cos(teta)),j+int(R*np.sin(teta))] += 1
                    
                        teta += np.pi/180
    return mat_centre

def max(matrice):
    dim = len(matrice)
    
    max_val = 0
    indices = np.zeros(dim)
    
    for d in range (0,dim):
        for i in range (0,len(matrice[d])):
            for j in range (0, len(matrice[d][i])):
                if(matrice[d,i,j]>max_val):
                    max_val = matrice[d,i,j]
                    indices = [d,i,j]
    return indices
        