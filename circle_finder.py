# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:36:08 2017

@author: boetto
"""
import numpy as np

pas_du_rayon = 10

def circle_finder(mat_cont):
    length = len(mat_cont[1])
    height = len(mat_cont)
    mat_centre = np.zeros((pas_du_rayon,height,length))
    
    for r in range (0,pas_du_rayon):    
        R = 20 + 5*r #Valeur incrémental du rayon, à modifier celon l'image à traiter (/!\ penser à modifier contour.py aussi)
        
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
    
    
    indices1 = np.zeros(dim)
#    indices2 = np.zeros(dim)
#    indices3 = np.zeros(dim)
    
    max1 = 0

    
    for d in range (0,dim):
        for i in range (0,len(matrice[d])):
            for j in range (0, len(matrice[d][i])):
                if(matrice[d,i,j]>max1):
#                    indices3=indices2
#                    indices2=indices1
                    
                    max1 = matrice[d,i,j]
                    indices1 = [d,i,j]
#    return [indices1,indices2,indices3]
    return indices1        