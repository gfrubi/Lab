# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
from scipy import stats
from matplotlib.patches import Ellipse # carga la librería para graficar elipses

fig = figure()
eje = fig.add_subplot(111, aspect='equal')
eje.set_xlim([-11, 11])
eje.set_ylim([-11, 11])

N=20 # número de puntos

x=stats.norm.rvs(loc=-7,size=N,scale=.6)
y=stats.norm.rvs(loc=-7,size=N,scale=.6)
eje.scatter(x,y)
eje.add_artist(Ellipse([-5,-5],width=2, height=2, angle=0, fill=False, color='r'))

x=stats.norm.rvs(loc=+5,size=N,scale=.6)
y=stats.norm.rvs(loc=-5,size=N,scale=.6)
eje.scatter(x,y)
eje.add_artist(Ellipse([+5,-5],width=2, height=2, angle=0, fill=False, color='r'))

x=stats.norm.rvs(loc=-8,size=N,scale=1.5)
y=stats.norm.rvs(loc=+8,size=N,scale=1.5)
eje.scatter(x,y)
eje.add_artist(Ellipse([-5,+5],width=2, height=2, angle=0, fill=False, color='r'))

x=stats.norm.rvs(loc=+5,size=N,scale=1.5)
y=stats.norm.rvs(loc=+5,size=N,scale=1.5)
eje.scatter(x,y)
eje.add_artist(Ellipse([+5,+5],width=2, height=2, angle=0, fill=False, color='r'))

eje.set_xlabel(r"aumento de la exactitud $\longrightarrow$")
eje.set_ylabel(ur"$\longleftarrow$ aumento de la precisión")
eje.get_xaxis().set_ticks([]) # oculta los ticks y los valores de x asociados
eje.get_yaxis().set_ticks([]) # oculta los ticks y los valores de y asociados
savefig("fig-ex-vs-prec.pdf")
