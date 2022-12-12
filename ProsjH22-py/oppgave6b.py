# oppgave6b.py

import random as rd
import numpy as np

kast = 21

liste = np.zeros(kast, dtype=int)

for i in range(kast):

    liste[i] = rd.randint(1,6)
    
print(liste)




