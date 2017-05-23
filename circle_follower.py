# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:40:46 2017

@author: aroux
"""

""" Initialisation des bibliothèques et fichier à importer"""
import cv2
import numpy as np

""" A TESTER !!! """


def new_position_finder (old_img, new_img, x_center, y_center, radius) : 
    """trouve la position du centre du cercle dans la nouvelle image    
        x_center = cleui de l'ancienne image, idem pour y_center
    """
    
    nbr_squares_x = 20  
    nbr_squares_y = 20 
    size_image_x = img.shape[0]
    size_image_y = img.shape[1]
    
    compteur = 0
    
    
    old_circle_square = np.zeros([2*radius, 2*radius])
    for k in range (2*radius) :
        for i in range (2*radius):
            old_circle_square[k,i] = old_img[k-x_center, i-y_center]
            
    #print(old_circle_square)
    matrice_distances = np.zeros([size_image_x-2*radius, size_image_y-2*radius])
    
    for i in range (0, size_image_x - 2*radius) : 
        for j in range (0, size_image_y - 2*radius):
            
            square_in_new = np.zeros([2*radius, 2*radius])
            
            for k in range (0, 2*radius) :
                for l in range (0, 2*radius) :
                    square_in_new[k,l] = new_img[i+k, j+l]
                    erreur_entre_pixels = (old_circle_square[k,l]-square_in_new[k,l])**2
                    matrice_distances[i,j] += erreur_entre_pixels
                    
                    #print(erreur_entre_pixels)
                    if(erreur_entre_pixels == 0):
                          compteur += 1
    print(i)
    print(j)
    print(k)
    print(l) 
    print(compteur)
          
    print(matrice_distances)
                    
                    
            
        
    
#    cv2.imshow('pièce', old_circle_square)
#    cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
#    cv2.destroyAllWindows() #on ferme tout
    

img = cv2.imread('pièce.jpeg', 0) #image noir et blanc de la pièce
    
    
new_position_finder(img, img, 150, 150, 2)
