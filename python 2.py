import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = np.array([2023, 2024,2025,2026])
data2 = np.array([100,1,300,40])

plt.title("STFU",fontsize =20,color = "#E70C0C"  )

line_style = dict(marker = ".",markersize = 30,
         markerfacecolor = "#070000",markeredgecolor = "black",
          linestyle = "dashed")

plt.plot(data1, data2,**line_style )
plt.show()

