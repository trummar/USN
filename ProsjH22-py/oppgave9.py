# oppgave8.py

import random as rd
import numpy as np

kast = 15000
liste = np.zeros(kast, dtype=int)

def kasting(kast):
   for i in range(kast):
       liste[i] = rd.randint(1,6) 
              
def resultater():
    svar_array = np.unique(liste, return_counts=True)

    res = svar_array[1]
    res = res/kast
    return res
       
kasting(kast)
relativ_frekvens_array = resultater()
print(relativ_frekvens_array)    



