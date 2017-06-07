# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:20:53 2017

@author: aroux
"""

""" importations et variables globales """
import cv2
import numpy as np
import gradient as grd
import floutage as flt
import image_resizer as ir
import circle_finder as cf

seuil_bas = 100   #seuils et valeurs de couleurs
seuil_haut = 150
black = 0
grey = 150
white = 255



""" Phase d'apprentissage : on apprend à reconnaitre les différentes pièces en fonction de leurs diamètres relatifs """

img = cv2.imread('1_euro_double.JPG', 0) #image noir et blanc de la pièce
img_resized = ir.image_resizer(img,0.1)
img_blurred = flt.blur_image(img_resized,13)

#on créé la matrice du gradient
mat_grad = grd.force_grad(img_blurred)

#on calcule les dimensions de l'image
length = len(img_blurred[1])
height = len(img_blurred)



#Détermination de la matrice des contours
print("Détermination de la matrice des contours")

mat_cont = np.zeros((height,length))
for i in range (1, height):
    for j in range (1, length):
        if (mat_grad[i,j]<seuil_bas):
            mat_cont [i,j] = white
        elif (mat_grad[i,j]>seuil_haut):
            mat_cont [i,j] = black
        else :
            mat_cont [i,j] = grey


#Elimination des pixels grisés
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

for i in range (1,height-1):
    for j in range (1,length-1):
        if (mat_cont[i,j] == grey):
            mat_cont[i,j] = white           

#Affinage du trait
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

#Recherche des cercle
print("Recherche des cercles")
number_of_circles_to_find = 2
final_circles = cf.circle_finder(mat_cont, number_of_circles_to_find)

#on les trie par ordre decroisant de TAILLE   
sorted_radius = np.zeros(5) #on y stocke les valeurs des rayons de pieces de 2 - 0.50 - 1 - 0.20 - 0.10 dans cet ordre
sorted_x = np.zeros(5) #idem avec les coordonnees x
sorted_y = np.zeros(5) #idem avec les coordonnees y

for k in range (number_of_circles_to_find) : 
    indice_of_max_so_far = np.argmax(final_circles[2,:])
    
    sorted_radius[k] = final_circles[2, indice_of_max_so_far]
    sorted_x[k] = final_circles[0, indice_of_max_so_far]
    sorted_y[k] = final_circles[1, indice_of_max_so_far]
    
    final_circles[2, indice_of_max_so_far] = 0 #sert a enlver le max de la liste
    
        
list_of_labels = ["2 euros", "50 cents", "1 euro", "20 cents", "10 cents"]

for k in range (number_of_circles_to_find) :
    x_center = int(sorted_x[k])
    y_center = int(sorted_y[k])
    radius = int(sorted_radius[k])

    cv2.circle(img_resized, (x_center, y_center), radius, (255,0,0))
    cv2.putText(img_resized, list_of_labels[k], (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0))

                       
cv2.imshow('img_resized with coins', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()  



""" maintenant on reconnait des pieces """







