#%% Forklarende tekst
"""
oppgave4d.py

Her bruker jeg lengre kommentarer for å beholde formatering 
og for å slippe å skrive hashtag for hver linje.

"""

streng = """
Dette 
kan være en
lengre tekst

"""
#%% bibliotek og variabler

import random as rd               # Importerer ressurs med aktuelle
import numpy as np                # funksjoner som trengs
        
kast = 21                         # setter antall kast til 21
# liste = np.array([])

liste = np.zeros(kast, dtype='U4') # oppretter et array med lengde 21 
                                   # bestående av nuller og klargjort
                                   # for strenger med lengde 4 som jo er 
                                   # lengden på "mynt" og "kron"
#%% For-løkke med if-setninger
for i in range(kast):              # En løkke som går 21 ganger

    tall = rd.randint(1,2)         # Velger et tilfeldig heltall fra og med 1
                                   # tilog med 2, altså 1 eller 2. 
    if tall == 1:                  # hvis-struktur som sjekker om trekt tall 
        # print("mynt")            # er 1 eller 2
        # liste = np.append(liste,"mynt")
        liste[i] = "mynt"          # Oppdaterer arrayet med stringen "mynt" på
                                   # plass i i arrayet
    elif tall == 2:
        # print("kron")
        # liste = np.append(liste,"kron")
        liste[i] = "kron"          # samme for her, men dersom 2 så "kron"
    else:
        print("Noko er gale")      # mulighet for feilsjekking

# %% avslutning og presentasjon
print(liste)                       # printer ut liste for å se kastene 
lengde = len(liste)                # sjekker at liste er lik lengde til 
                                   # antall kast
print(lengde)
print(streng)                      # vise at formatering med triple """ funker.  






#%%