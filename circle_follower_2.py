# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:40:46 2017

@author: aroux
"""

""" Initialisation des bibliothèques et fichier à importer"""
import cv2
import numpy as np
import image_resizer as imres


def new_position_finder (old_img, new_img, x_center, y_center, radius) : 
    """trouve la position du centre du cercle dans la nouvelle image    
        x_center = cleui de l'ancienne image, idem pour y_center
    """
    
    size_image_x = old_img.shape[0]
    size_image_y = old_img.shape[1]
    
    print(size_image_x)
    print(size_image_y)
    
#    cv2.circle(old_img, (x_center, y_center), radius, (0,0,255))
#    cv2.imshow('pièce', old_img)
#    cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
#    cv2.destroyAllWindows() #on ferme tout
#    

    
    old_circle_square = np.zeros([2*radius+1, 2*radius+1])
    for i in range (2*radius+1) :
        for k in range (2*radius+1):
            old_circle_square[i,k] = old_img[y_center-radius+i, x_center-radius+k]
            
    print("motif a retrouver : ")
    print(old_circle_square)
    print("\n")
    
    matrice_distances = np.zeros([size_image_x-2*radius, size_image_y-2*radius])
        
    for i in range (0, size_image_x-2*radius) : 
        print("Progression =", (i+1), "sur", (size_image_x-2*radius))
        print("\n")
        for j in range (0, size_image_y-2*radius):
            
            square_in_new = new_img[i:i+2*radius+1, j:j+2*radius+1]
            
            matrice_distances[i,j] = np.linalg.norm(square_in_new - old_circle_square)
            
#            for k in range (0, 2*radius) :
#                for l in range (0, 2*radius) :             
#                    
#                    erreur_entre_pixels = (old_circle_square[k,l]-square_in_new[k,l])**2
#                    matrice_distances[i,j] += erreur_entre_pixels
                    
         
    print("matrice des distances")
    print(matrice_distances)
    #la position du 0 dans matcrice_distances nous donne le deplacement du motif
    
    #il faut maintenant trouver sa position
    """ A CHANGER """
    indice_min = np.argmin(matrice_distances)#il correspond à la postion en mode liste
    new_pos_x = (indice_min) % (size_image_y)
    new_pos_y = (indice_min) // (size_image_y)
    print('new_pos_x :',new_pos_x, 'new_pos_y :', new_pos_y)
    
    
               
#    cv2.circle(new_img, (new_pos_x, new_pos_y), 25, (0,0,255))  
#    cv2.imshow('pièce', new_img)
#    cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
#    cv2.destroyAllWindows() #on ferme tout
    



test = 2

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
    
    img2 = np.array([[1,2,3,0,0],[4,5,6,0,0],[7,8,9,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    img1 = np.array([[0,0,0,0,0],[0,0,1,2,3],[0,0,4,5,6],[0,0,7,8,9],[0,0,0,0,0]])
    
    print("ancienne image")
    print(img1)
    print("\n")
    print("nouvelle image")
    print(img2)
    print("\n")
        
    new_position_finder(img1, img2, 3, 2, 1)

if test == 4 : 
    img1 = cv2.imread('photo1new.JPG', 0) #image noir et blanc de la pièce
    img2 = cv2.imread('photo2new.JPG', 0) #image noir et blanc de la pièce
    
    img1 = imres.image_resizer(img1, 0.1)
    img2 = imres.image_resizer(img2, 0.1)
    
    new_position_finder(img1, img2, 85, 165, 50)
