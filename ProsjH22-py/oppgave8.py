# oppgave8.py

import random as rd
import numpy as np

kast = 1500000
liste = np.zeros(kast, dtype=int)

for i in range(kast):
    liste[i] = rd.randint(1,6)    

svar_array = np.unique(liste, return_counts=True)

resultater = svar_array[1]
resultater = resultater/kast
print(resultater)


