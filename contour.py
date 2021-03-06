# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:39:04 2017

@author: boetto
"""
""" Initialisation des bibliothèques et fichier à importer"""
import cv2
import numpy as np

import gradient as grd
import floutage as flt
import image_resizer as ir

import circle_finder as cf

"""Variables globales"""
img = cv2.imread('1_euro_double.JPG', 0) #image noir et blanc de la pièce
img_resized = ir.image_resizer(img,0.1)
img_blurred = flt.blur_image(img_resized,13)


cv2.imshow('img_blurred', img_blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()

mat_grad = grd.force_grad(img_blurred)


"""Dimension de l'image"""
length = len(img_blurred[1])
height = len(img_blurred)

"""seuils et valeurs de couleurs"""
seuil_bas = 100 #330
seuil_haut = 150
black = 0
grey = 150
white = 255

mat_cont = np.zeros((height,length))
#mat_force_grad = grd.force_grad(img)

"""Détermination de la matrice des contours""" 
print("Détermination de la matrice des contours")

for i in range (1, height):
    for j in range (1, length):
        if (mat_grad[i,j]<seuil_bas):
            mat_cont [i,j] = white
        elif (mat_grad[i,j]>seuil_haut):
            mat_cont [i,j] = black
        else :
            mat_cont [i,j] = grey


"""Elimination des pixels grisées"""
print("Elimination des pixels grisés")
compteur = 1
still_grey = 1
while(still_grey==1 and compteur<100):
    still_grey = 0
    for i in range (1,height-1): 
        for j in range (1,length-1):
            if (mat_cont[i,j] == grey): #on analyse toutes les pixels grises
                if (mat_cont[i+1,j]==black or mat_cont[i-1,j] == black or mat_cont[i,j+1]==black or mat_cont[i,j-1]==black): #s'il y a une pixel noir voisine alors la pixel grise devient noir
                    mat_cont[i,j] = black
                elif (mat_cont[i+1,j]==grey or mat_cont[i-1,j] == grey or mat_cont[i,j+1]==grey or mat_cont[i,j-1]==grey):
                    still_grey = 1; #on ne peut rien dire pour cett pixel donc on la laisse grise et on maintient still_grey à 1 pour affiner l'image une nouvelle fois
                else :
                    mat_cont[i,j]=white
    compteur += 1
    #cv2.imshow('pièce', mat_cont)
    #cv2.waitKey(0)*
for i in range (1,height-1):
    for j in range (1,length-1):
        if (mat_cont[i,j] == grey):
            mat_cont[i,j] = white

cv2.imshow('mat_cont', mat_cont)
cv2.waitKey(0)
cv2.destroyAllWindows()            

"""Affinage du trait"""
print("Affinage du trait")
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

cv2.imshow('mat_cont', mat_cont)
cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
cv2.destroyAllWindows() #on ferme tout


"""Recherche des cercle"""
print("Recherche des cercle")
number_of_circles_to_find = 2
final_circles = cf.circle_finder(mat_cont, number_of_circles_to_find)


for k in range (number_of_circles_to_find) :
    x_center = int(final_circles[0, k])
    y_center = int(final_circles[1, k])
    radius = int(final_circles[2, k])

    cv2.circle(img_resized, (x_center, y_center), radius, (255,0,0))  

                         
cv2.imshow('img_resized with coins', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()  






   