# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:36:08 2017

@author: boetto
"""
import numpy as np



start_radius = 30
step_radius = 3
number_of_radius_tested = 20

def circle_finder(mat_cont, number_of_circles_to_find):
    """ fonction qui trouve le cercle en testant différents rayons possibles
        retourne les coordonnees du centre et le rayon de tous les cercles trouvés
        sous la forme : [x, y, rayon] """
    length = len(mat_cont[1])
    height = len(mat_cont)
    mat_centre = np.zeros((number_of_radius_tested, height,length))
            
    for r in range (0,number_of_radius_tested):    
        R = start_radius + step_radius*r #Valeur incrémentale du rayon, à modifier celon l'image à traiter (/!\ penser à modifier contour.py aussi)
        
        for i in range (0,height):
            for j in range (0,length):
                teta = 0
                     
                
                if(mat_cont[i,j]==0 and i != 0 and j != 0): #je suis un point noir
                                    
                    while (teta < 2*np.pi): #parcourt du paramètre teta de 0 à 2*pi
                                                
                        if(0 <= i+R*np.cos(teta) and i+R*np.cos(teta) < height and 0 <= j+R*np.sin(teta) and j+R*np.sin(teta) < length and i != 0 and j != 0): #on vérifie qu'on est dans la matrice
                        
                            #if(int(R*np.cos(teta))!= int(R*np.cos(teta)) or int(R*np.sin(teta))!= int(R*np.sin(teta-180/np.pi))): #on s'assure de ne pas incrémenter deux fois le même "centre"
                            mat_centre[r,i+int(R*np.cos(teta)),j+int(R*np.sin(teta))] += 1
                    
                        teta += np.pi/180
                        
    #####                 

    vect_of_centers = np.zeros((3, number_of_radius_tested, number_of_circles_to_find))
    
    for k in range (0, number_of_radius_tested) :
        #dans cette boucle, on stocke les valeur des centres pour chaque rayon testé
        
        for i in range (number_of_circles_to_find) :        
        
            indiceMax_so_far = np.argmax(mat_centre[k])
            max_value_so_far = np.max(mat_centre[k])

            x_max = indiceMax_so_far // length
            y_max = indiceMax_so_far % length
            
            vect_of_centers[0,k,i] = x_max
            vect_of_centers[1,k,i] = y_max
            vect_of_centers[2,k,i] = max_value_so_far
            
            #on enleve maintenant le max qu'on vient de traiter
            mat_centre[k, x_max-20:x_max+20, y_max-20:y_max+20] = 0
    
    final_circles = np.zeros((3, number_of_circles_to_find))
    
    for k in range (number_of_circles_to_find) :
        k_ieme_circle = vect_of_centers[:,:,k]     
        index_of_max_value_found = np.argmax(k_ieme_circle[2,:])     
        
        y_center = int(vect_of_centers[0, index_of_max_value_found, k])  
        x_center = int(vect_of_centers[1, index_of_max_value_found, k])
        radius = int(start_radius + step_radius * index_of_max_value_found)
        
        final_circles[0, k] = x_center
        final_circles[1, k] = y_center #attention, pour une raison inconnus, il faut les inverser à cet endroit là
        final_circles[2, k] = radius
 
    return final_circles



def max(matrice):
    dim = len(matrice)
    indices1 = np.zeros(dim)
    max1 = 0

    for d in range (0,dim):
        for i in range (0,len(matrice[d])):
            for j in range (0, len(matrice[d][i])):
                if(matrice[d,i,j]>max1):
                    max1 = matrice[d,i,j]
                    indices1 = [d,i,j]
                    
    return indices1        