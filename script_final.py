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
import grey_pixel_eliminator as gpe
import line_width_reducer as lwr

seuil_bas = 100   #seuils et valeurs de couleurs
seuil_haut = 150
black = 0
grey = 150
white = 255

images_names = ["unknown_0.JPG", "unknown_1.JPG", "unknown_2.JPG"]
#images_names = ["unknown_0.JPG", "unknown_1","unknown_2", "unknown_3","unknown_4"]
number_of_coins_to_identify = len(images_names)



""" Phase d'apprentissage : on apprend à reconnaitre les différentes pièces en fonction de leurs diamètres relatifs """

img = cv2.imread('3_coins.JPG', 0) #image noir et blanc de la pièce
img_resized = ir.image_resizer(img,0.2)
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
print("Elimination des pixels gris")     
mat_cont = gpe.grey_pixel_eliminator(mat_cont, white, grey, black)
   

#Affinage du trait
print("Affinage du trait")
mat_cont = lwr.line_width_reducer(mat_grad, mat_cont, img)

cv2.imshow('mat_cont', mat_cont)
cv2.imwrite('FINAL_mat_cont.png', mat_cont)
cv2.waitKey(0)
cv2.destroyAllWindows()  
    

#Recherche des cercle
print("Recherche des cercles")
number_of_circles_to_find = 3
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
    
        
list_of_labels = ["50 cents", "1 euro", "10 cents"]

for k in range (number_of_circles_to_find) :
    x_center = int(sorted_x[k])
    y_center = int(sorted_y[k])
    radius = int(sorted_radius[k])

    cv2.circle(img_resized, (x_center, y_center), radius, (255,0,0))
    cv2.putText(img_resized, list_of_labels[k], (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0))

                       
cv2.imshow('img_resized with coins', img_resized)
cv2.imwrite('FINAL_resultat_apprentissage.png', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()  



""" Maintenant on reconnait des pieces """

for k in range (number_of_coins_to_identify) :
    img = cv2.imread(images_names[k], 0) #image noir et blanc de la pièce inconnue
    img_resized = ir.image_resizer(img,0.2)
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
    mat_cont = gpe.grey_pixel_eliminator(mat_cont, white, grey, black)
       
    #Affinage du trait
    print("Affinage du trait")
    mat_cont = lwr.line_width_reducer(mat_grad, mat_cont, img)
    
    #Recherche des cercle
    print("Recherche des cercles")
    number_of_circles_to_find = 1
    final_circles = cf.circle_finder(mat_cont, number_of_circles_to_find)
    
    #on détermine sa valeur en regardant de quel rayon existant elle est le plus proche
    x_center = final_circles[0]
    y_center = final_circles[1]
    radius = final_circles[2]
    radius_differences = np.zeros(5)
    
    for k in range (len(list_of_labels)) : 
        radius_differences[k] = (radius - sorted_radius[k])**2
        
    label_of_coin = list_of_labels[np.argmin(radius_differences)-1]
    
    cv2.circle(img_resized, (x_center, y_center), radius, (255,0,0))
    cv2.putText(img_resized, label_of_coin, (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0))                 
   
    cv2.imshow('identified coin', img_resized)
    cv2.imwrite('FINAL_10_cents_identified.png', img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    
    
    

        
    
    
    
    
    
