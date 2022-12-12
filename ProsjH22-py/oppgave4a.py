# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:30:11 2022

@author: vande
"""


import random as rd

liste = []

for i in range(21):

    tall = rd.randint(1,2)
    
    if tall == 1:
        # print("mynt")
        liste.append("mynt")
        
    elif tall == 2:
        # print("kron")
        liste.append("kron")
    else:
        print("Noko er gale")


print(liste)
lengde = len(liste)
print(lengde)




