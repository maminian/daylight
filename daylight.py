import numpy as np
from matplotlib import pyplot as plt

day = np.arange(366)
lat = np.arange(0,91)

axis = 23.439 # in degrees

X,Y = np.meshgrid(day, lat)

M = 1 - np.tan(Y*np.pi/180)*np.tan(axis*np.pi/180*np.cos(np.pi/182.625*X))

M = np.minimum(M,2)
M = np.maximum(M,0)

b = np.arccos(1-M)/np.pi*24

fig,ax = plt.subplots(figsize=(8,4), constrained_layout=True)

duh = ax.contourf(X,Y,b, levels=np.arange(0,25), cmap=plt.cm.inferno)

levs = np.array([1,6,12,18,23])
levcols = plt.cm.inferno(levs/24)**0.5

duh2 = ax.contour(X,Y,b, levels=levs, colors=levcols, linestyles='--', linewidths=2)

fig.colorbar(duh)
cax = fig.get_axes()[-1] # colorbar, hopefully

ax.set(xlabel='Day of year', ylabel='Latitude (degrees)')

fig.colorbar(duh2, cax=cax)
fig.show()

