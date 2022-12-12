# oppgave8.py

# sannsynlighet/rel.frekv for å få en firer...

import random as rd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

total_kast = 720
liste = np.zeros(total_kast, dtype=int)
y_arr = np.zeros((total_kast//6), dtype=float)
x_arr = np.linspace(0, total_kast,(total_kast//6))

vis_nummer = "hvordan relativ frekvens varierer"

def kasting(kast):
   for i in range(kast):
       liste[i] = rd.randint(1,6) 
              
def resultater():
    svar_array = np.unique(liste, return_counts=True)
    res = svar_array[1]
    res = res/kast
    return res

for index,j in enumerate(range(6,total_kast + 1, 6)):
    kast = j 
    kasting(j)
    new_arr = resultater()
    y_arr[index] = new_arr[3]
    
data = np.array([x_arr,y_arr])
dataset = pd.DataFrame({'x-verier': data[0, :], 'y-verdier': data[1, :]})
dataset.to_csv("plottedata_pandas_KOMMA.csv")
dataset.to_excel("plottedata_pandas_EXCEL.xlsx")

plt.plot(x_arr, y_arr)
plt.savefig("plot.png")
plt.legend([vis_nummer])
plt.show()








