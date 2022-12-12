# oppgave7.py

import random as rd
import numpy as np

kast = 21

enere = 0
toere = 0
treere = 0
firere = 0
femmere = 0
seksere = 0

liste = np.zeros(kast, dtype=int)

for i in range(kast):

    liste[i] = rd.randint(1,6)
    
# print(liste)

for j in liste:
    
    if j == 1:
        enere = enere + 1
    
    elif j == 2:
        toere = toere + 1
        
    elif j == 3:
        treere += 1
    
    elif j == 4:
        firere += 1
        
    elif j == 5:
        femmere += 1
        
    elif j == 6:
        seksere += 1
    
    else:
        print("Feil!!")
        
print("Under er antall:")
print("1,2,3,4,5,6:")
print("*************")
print(enere, toere, treere, firere, femmere, seksere)  
    


