# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:27:03 2017

@author: boetto
"""

import cv2

img = cv2.imread('pièce.jpeg',0) #importation de la photo et mise en noir et blanc

cv2.imshow('pièce', img) #affichage de l'image
cv2.waitKey(0) #on attend que l'utilisateur appuye sur une touche pour agir
cv2.destroyAllWindows() #on ferme tout