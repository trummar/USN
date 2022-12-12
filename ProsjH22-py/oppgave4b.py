# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:30:11 2022

@author: vande
"""


import random as rd
import numpy as np

kast = 21
# liste = np.array([])

liste = np.zeros(kast, dtype='U4')

for i in range(kast):

    tall = rd.randint(1,2)
    
    if tall == 1:
        # print("mynt")
        # liste = np.append(liste,"mynt")
        liste[i] = "mynt"
        
    elif tall == 2:
        # print("kron")
        # liste = np.append(liste,"kron")
        liste[i] = "kron"
    else:
        print("Noko er gale")


print(liste)
lengde = len(liste)
print(lengde)




