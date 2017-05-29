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
    size_image_x = old_img.shape[0]
    size_image_y = old_img.shape[1]
    

    
    compteur = 0
    
    
    old_circle_square = np.zeros([2*radius+1, 2*radius+1])
    for i in range (2*radius+1) :
        for k in range (2*radius+1):
            old_circle_square[i,k] = old_img[y_center-radius+i, x_center-radius+k]
            
    print("motif a retrouver : ")
    print(old_circle_square)
    print("\n")
    
    matrice_distances = np.zeros([size_image_x-2*radius, size_image_y-2*radius])
        
    for i in range (0, size_image_x - 2*radius) : 
        for j in range (0, size_image_y - 2*radius):
            
            square_in_new = np.zeros([2*radius+1, 2*radius+1])
            
            for k in range (0, 2*radius+1) :
                for l in range (0, 2*radius+1) :
                    square_in_new[k,l] = new_img[i+k, j+l]                 
                    
                    erreur_entre_pixels = (old_circle_square[k,l]-square_in_new[k,l])**2
                    matrice_distances[i,j] += erreur_entre_pixels
                    
                    #print(erreur_entre_pixels)
                    if(erreur_entre_pixels == 0):
                          compteur += 1
         
    print("matrice des distances")
    print(matrice_distances)
    #la position du 0 dans matcrice_distances nous donne le deplacement du motif
    
    #il faut maintenant trouver sa position
    indice_min = np.argmin(matrice_distances) #il correspond à la postion en mode liste
    deplacement_x = (indice_min) % (size_image_y-2*radius)
    deplacement_y = (indice_min) // (size_image_y-2*radius)
    print('deplacement_x :',deplacement_x, 'deplacement_y :', deplacement_y)
                    
            
        
    
#    cv2.imshow('pièce', old_circle_square)
#    cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
#    cv2.destroyAllWindows() #on ferme tout
    

img = cv2.imread('pièce.jpeg', 0) #image noir et blanc de la pièce

test = 3

if test == 1 : 

    img1 = np.array([[1,2,3,0,0],[4,5,6,0,0],[7,8,9,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    img2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,2,3,0,0],[4,5,6,0,0],[7,8,9,0,0]])

    print("ancienne image")
    print(img1)
    print("\n")
    print("nouvelle image")
    print(img2)
    print("\n")
    
    new_position_finder(img1, img2, 1, 1, 1)
    
if test == 2 : 

    img1 = np.array([[1,2,3,0,0],[4,5,6,0,0],[7,8,9,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    img2 = np.array([[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]])

    print("ancienne image")
    print(img1)
    print("\n")
    print("nouvelle image")
    print(img2)
    print("\n")
    
    new_position_finder(img1, img2, 1, 1, 1)

if test == 3 : 
    
    img1 = np.array([[1,2,3,0,0],[4,5,6,0,0],[7,8,9,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    img2 = np.array([[0,0,0,0,0],[0,0,1,2,3],[0,0,4,5,6],[0,0,7,8,9],[0,0,0,0,0]])
    
    print("ancienne image")
    print(img1)
    print("\n")
    print("nouvelle image")
    print(img2)
    print("\n")
        
    new_position_finder(img1, img2, 1, 1, 1)
