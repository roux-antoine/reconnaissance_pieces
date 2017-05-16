# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:34:13 2017

@author: aroux
"""

def mean_color_finder(img, circle):
    """ trouve la couleur moyenne dans le carre circonscrit au cercle
        attention : circle est un array de la forme [xCentre, yCentre, rayon]"""
        
        xCenter = circle[0]
        yCenter = circle[1]
        radius = circle[2]
        
        
        rectOfInterest = img[xCenter-radius:xCenter+radius, yCenter-radius:yCenter+radius]
        
        
        
        
        