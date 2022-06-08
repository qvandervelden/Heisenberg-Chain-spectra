import numpy as np
import matplotlib.pyplot as plt

filename_data = 'Spectrum-16x0.5c.txt'
filename_plot = 'plot-Spectrum-18x0.5.png'

plt.figure()

E = np.genfromtxt(filename_data)
plt.scatter(E[:,1], E[:,0], marker='_', linewidths=0.5)

plt.xlabel('spin')
plt.ylabel('energy')
plt.show()
        