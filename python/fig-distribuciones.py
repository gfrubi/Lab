# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from scipy import stats
from numpy import *
from matplotlib.patches import Ellipse # carga la librería para graficar elipses

fig = figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_artist(Ellipse([0,0],width=5, height=10, angle=-45, fill=False, color='r'))
ax.set_xlim([-5.5, 5.5])
ax.set_ylim([-5.5, 5.5])
N=500 # número de puntos
x=stats.norm.rvs(size=N) 
y=stats.norm.rvs(size=N,scale=2)
# rota en 45 grados
xr=(x-y)/sqrt(2)
yr=(-x-y)/sqrt(2)
ax.scatter(xr,yr)
ax.scatter(0,0,s=60, c='r')
savefig("fig-1x2rot2.pdf")
