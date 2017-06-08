# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:07:05 2017

@author: aroux
"""


def grey_pixel_eliminator(mat_cont, white, grey, black):
    """ prend en arg la matrice des contours et les seuils
        enlève les pixels gris en les transformant en pixels blancs ou noirs """

    compteur = 1
    still_grey = 1
    length = len(mat_cont[1])
    height = len(mat_cont)
    
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
    
    return mat_cont