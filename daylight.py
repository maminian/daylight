import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker, dates
import datetime

#
day = np.arange(365)+10 # shift for winter solstice
date_of_year = [datetime.datetime(2023, 1,1) + datetime.timedelta(days=int(i)-10) for i in day]
lat = np.arange(0,91)

axis = 23.439 # in degrees

X,Y = np.meshgrid(day, lat)

M = 1 - np.tan(Y*np.pi/180)*np.tan(axis*np.pi/180*np.cos(np.pi/182.625*X))

M = np.clip(M, 0, 2)

b = np.arccos(1-M)/np.pi*24

if __name__=="__main__":
    fig,ax = plt.subplots(figsize=(8,4), constrained_layout=True)

    duh = ax.contourf(date_of_year,lat,b, levels=np.arange(0,25), cmap=plt.cm.inferno)

    levs = np.array([1,6,12,18,23])
    levcols = plt.cm.inferno(levs/24)**0.5

    duh2 = ax.contour(date_of_year,lat,b, levels=levs, colors=levcols, linestyles='--', linewidths=2)

    #

    fig.colorbar(duh)
    cax = fig.get_axes()[-1] # colorbar, hopefully
    fig.colorbar(duh2, cax=cax)
    

    ax.xaxis.set_major_locator(dates.MonthLocator(bymonth=range(3,13,3), bymonthday=21))
    ax.xaxis.set_minor_locator(dates.MonthLocator(interval=1, bymonthday=21))
    ax.xaxis.set_major_formatter(dates.DateFormatter('%b %d'))

    ax.set(xlabel='Day of year', ylabel='Latitude (degrees)')
#    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.grid(which='major', c=[1,1,1,0.5], lw=0.5)
    ax.grid(which='minor', c=[1,1,1,0.2], lw=0.2)

    fig.show()

