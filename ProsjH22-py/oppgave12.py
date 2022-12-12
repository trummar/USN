

# oppgave12.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

vis_nummer = "Test"

new_set = pd.read_excel("plottedata_pandas_EXCEL.xlsx")
# print(new_set)

new_arr = new_set.to_numpy()

plt.plot(new_arr[:,1], new_arr[:,2])
plt.savefig("plot.png")
plt.legend([vis_nummer])
plt.show()

