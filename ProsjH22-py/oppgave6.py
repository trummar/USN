# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:30:11 2022

@author: vande
"""
# oppgave4b.py

import random as rd
import numpy as np

kast = 21
# liste = np.array([])

liste = np.zeros(kast, dtype=int)

for i in range(kast):

    tall = rd.randint(1,6)
    
    if tall == 1:
        # print("mynt")
        # liste = np.append(liste,"mynt")
        liste[i] = tall
        
    elif tall == 2:
        # print("kron")
        # liste = np.append(liste,"kron")
        liste[i] = tall
        
    elif tall == 3:
         # print("mynt")
         # liste = np.append(liste,"mynt")
         liste[i] = tall
         
    elif tall == 4:
         # print("kron")
         # liste = np.append(liste,"kron")
         liste[i] = tall
         
         
    elif tall == 5:
          # print("mynt")
          # liste = np.append(liste,"mynt")
          liste[i] = tall
          
    elif tall == 6:
          # print("kron")
          # liste = np.append(liste,"kron")
          liste[i] = tall
         
    else:
        print("Noko er gale")


print(liste)




