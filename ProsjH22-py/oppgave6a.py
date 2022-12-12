# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:30:11 2022

@author: vande
"""
# oppgave4b.py

import random as rd
import numpy as np

kast = 21

liste = np.zeros(kast, dtype=int)

for i in range(kast):

    tall = rd.randint(1,6)
    
    if tall == 1:
        liste[i] = tall
        
    elif tall == 2:
        liste[i] = tall
        
    elif tall == 3:       
         liste[i] = tall
         
    elif tall == 4:        
         liste[i] = tall
                  
    elif tall == 5:        
          liste[i] = tall
          
    elif tall == 6:      
          liste[i] = tall
        
    else:
        print("Noko er gale")


print(liste)




