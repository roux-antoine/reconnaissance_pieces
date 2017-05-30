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

import circle_finder as cf

"""Variables globales"""
img = cv2.imread('pièce.jpeg', 0) #image noir et blanc de la pièce
img = flt.blur_image(img,13)


mat_grad = grd.mat_grad(img)


"""Dimension de l'image"""
length = len(img[1])
height = len(img)

"""seuils et valeurs de couleurs"""
seuil_bas = 300 #330
seuil_haut = 350
black = 0
grey = 150
white = 255

mat_cont = np.zeros((height,length))


"""Détermination de la matrice des contours""" 
print("Détermination de la matrice des contours")

for i in range (1, height):
    for j in range (1, length):
        if (grd.force_grad(img,i,j)<seuil_bas):
            mat_cont [i,j] = white
        elif (grd.force_grad(img,i,j)>seuil_haut):
            mat_cont [i,j] = black
        else :
            mat_cont [i,j] = grey


"""Affinage des pixels grisées"""
print("Affinage des pixels grisés")
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
                
        if (grd.angle_grad(img,i,j)<=-67,5 or 67,5<=grd.force_grad(img,i,j)):
            if (mat_grad[i-1,j]>mat_grad[i,j] or mat_grad[i+1,j]>mat_grad[i,j]):
                mat_cont[i,j] = 255
                
        if (-67,5<grd.angle_grad(img,i,j) and grd.angle_grad(img,i,j)<-22,5 ):
            if (mat_grad[i+1,j+1]>mat_grad[i,j] or mat_grad[i-1,j-1]>mat_grad[i,j]):
                mat_cont[i,j] = 255

print("fini")

cv2.imshow('pièce', mat_cont)
cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
cv2.destroyAllWindows() #on ferme tout


mat_centre = cf.circle_finder(mat_cont)
print(mat_centre)

max1 = cf.max(mat_centre)
mat_centre[max1[0], max1[1]-20:max1[1]+20, max1[2]-20:max1[2]+20] = 0

max2 = cf.max(mat_centre)
mat_centre[max2[0], max2[1]-20:max2[1]+20, max2[2]-20:max2[2]+20] = 0

max3 = cf.max(mat_centre)
mat_centre[max3[0], max3[1]-20:max3[1]+20, max3[2]-20:max3[2]+20] = 0

MAXS=[max1,max2,max3]
print(MAXS)


if (MAXS[0][0]>=MAXS[1][0] and MAXS[0][0]>=MAXS[2][0]):
    MAX = MAXS[0]
elif (MAXS[1][0]>=MAXS[0][0] and MAXS[1][0]>=MAXS[2][0]):
    MAX = MAXS[1]
else:
    MAX = MAXS[2]



cv2.circle(mat_cont, (MAX[1], MAX[2]), 40 + 10*MAX[0],(0,0,255))

cv2.imshow('pièce', mat_cont)
cv2.waitKey(0)
cv2.destroyAllWindows()
