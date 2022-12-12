# oppgave8.py

# sannsynlighet/rel.frekv for å få en firer...

import random as rd
import numpy as np
import matplotlib.pyplot as plt

def kasting(kast):
   for i in range(kast):
       liste[i] = rd.randint(1,6) 
              
def resultater():
    svar_array = np.unique(liste, return_counts=True)
    res = svar_array[1]
    res = res/kast
    return res

"""
Dette programmet oppretter et stort antall filer ved
et stort antall kast.
"""

total_filer = 36
total_kast = total_filer * 6
filnavn = "plots/plot"
filnavn_ende = ".png"

liste = np.zeros(total_kast, dtype=int)
y_arr = np.zeros((total_kast//6), dtype=float)
x_arr = np.linspace(0, total_kast,(total_kast//6))


for thindex in range(0,total_filer + 1 ,1):
    
    vis_nummer = str(thindex)
    string_dex = str(thindex)
    new_filename = filnavn + string_dex + filnavn_ende
    # print(new_filename)
    
    
    """
    for index,j in enumerate(range(6,total_kast + 1, 6)):
        kast = j 
        kasting(j)
        new_arr = resultater()
        y_arr[index] = new_arr[3]
    """
    
    
    plt.plot(x_arr[0:], y_arr)
    plt.ylim([0.05,0.30])
    plt.savefig(new_filename)
    plt.legend([vis_nummer])
    plt.show()








