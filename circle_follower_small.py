# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:40:46 2017

@author: aroux
"""

""" Initialisation des bibliothèques et fichier à importer"""
import cv2
import numpy as np


def new_position_finder (old_img, new_img, x_center, y_center, radius) : 
    """trouve la position du centre du cercle dans la nouvelle image    
        x_center = cleui de l'ancienne image, idem pour y_center
    """
    
    scale = 10
    size_image_x = old_img.shape[0]
    size_image_y = old_img.shape[1]
    
    print(size_image_x)
    print(size_image_y)
    
    old_img_small = cv2.resize(old_img, (size_image_x/scale, size_image_x/scale), interpolation = cv2.INTER_AREA)
    new_img_small = cv2.resize(new_img, (size_image_x/scale, size_image_x/scale), interpolation = cv2.INTER_AREA)
    x_center_small = int(x_center/scale)
    y_center_small = int(y_center/scale)
    radius_small = int(radius/scale)

    size_image_small_x = old_img_small.shape[0]
    size_image_small_y = old_img_small.shape[1]
    
    old_circle_square = np.zeros([2*radius_small+1, 2*radius_small+1])
    for i in range (2*radius_small+1) :
        for k in range (2*radius_small+1):
            old_circle_square[i,k] = old_img_small[y_center_small-radius_small+i, x_center_small-radius_small+k]
            
    print("motif a retrouver : ")
    print(old_circle_square)
    print("\n")
    
    matrice_distances = np.zeros([size_image_small_x-2*radius_small, size_image_y-2*radius_small])
        
    for i in range (0, size_image_small_x - 2*radius_small) : 
        print("Progression =", (i+1), "sur", (size_image_small_x - 2*radius_small))
        print("\n")
        for j in range (0, size_image_small_y - 2*radius_small):
            
            square_in_new = np.zeros([2*radius_small+1, 2*radius_small+1])
            
            for k in range (0, 2*radius_small+1) :
                for l in range (0, 2*radius_small+1) :
                    square_in_new[k,l] = new_img_small[i+k, j+l]                 
                    
                    erreur_entre_pixels = (old_circle_square[k,l]-square_in_new[k,l])**2
                    matrice_distances[i,j] += erreur_entre_pixels
                    
         
    print("matrice des distances")
    print(matrice_distances)
    #la position du 0 dans matcrice_distances nous donne le deplacement du motif
    
    #il faut maintenant trouver sa position
    indice_min = np.argmin(matrice_distances) #il correspond à la postion en mode liste
    deplacement_x = (indice_min) % (size_image_y-2*radius)
    deplacement_y = (indice_min) // (size_image_y-2*radius)
    print('deplacement_x :',deplacement_x, 'deplacement_y :', deplacement_y)
    
    
#    new_circle_square = np.zeros([2*radius_small+1, 2*radius_small+1])
#    for i in range (deplacement_x, 2*radius_small+1 + deplacement_x) :
#        for k in range (deplacement_y, 2*radius_small+1 + deplacement_y):
#            new_circle_square[i,k] = new_img_small[y_center_small-radius_small+i, x_center_small-radius_small+k]
#                    
           
        
    cv2.imshow('pièce', old_circle_square)
    cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
    cv2.destroyAllWindows() #on ferme tout
    



test = 4

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

if test == 4 : 
    img1 = cv2.imread('1_euro_avant.JPG', 0) #image noir et blanc de la pièce
    img2 = cv2.imread('1_euro_apres.JPG', 0) #image noir et blanc de la pièce
    new_position_finder(img1, img2, 1500, 2000, 30)
