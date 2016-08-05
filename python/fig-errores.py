# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

datbabs = genfromtxt("datos-ba-bs.txt")
fig, eje = subplots(1,1)
x=datbabs[:,0]
y=datbabs[:,1]
eje.bar(x,y,align="center")
eje.set_xlabel("Variable aleatoria")
eje.set_ylabel(u"Número de ocurrencias")
eje.set_title(u"a) Bajo error aleatorio, bajo error sistemático")
eje.set_xlim([0,20])
eje.set_ylim([0,16])
fig.savefig("fig-ba-bs.pdf")

datbaas = genfromtxt("datos-ba-as.txt")
fig, eje = subplots(1,1)
x=datbaas[:,0]
y=datbaas[:,1]
eje.bar(x,y,align="center")
eje.set_xlabel("Variable aleatoria")
eje.set_ylabel(u"Número de ocurrencias")
eje.set_title(u"b) Bajo error aleatorio, alto error sistemático")
eje.set_xlim([0,20])
eje.set_ylim([0,16])
fig.savefig("fig-ba-as.pdf")

dataabs = genfromtxt("datos-aa-bs.txt")
fig, eje = subplots(1,1)
x=dataabs[:,0]
y=dataabs[:,1]
eje.bar(x,y,align="center")
eje.set_xlabel("Variable aleatoria")
eje.set_ylabel(u"Número de ocurrencias")
eje.set_title(u"c) Alto error aleatorio, bajo error sistemático")
eje.set_xlim([0,20])
eje.set_ylim([0,16])
fig.savefig("fig-aa-bs.pdf")

dataaas = genfromtxt("datos-aa-as.txt")
fig, eje = subplots(1,1)
x=dataaas[:,0]
y=dataaas[:,1]
eje.bar(x,y,align="center")
eje.set_xlabel("Variable aleatoria")
eje.set_ylabel(u"Número de ocurrencias")
eje.set_title(u"d) Alto error aleatorio, alto error sistemático")
eje.set_xlim([0,20])
eje.set_ylim([0,16])
fig.savefig("fig-aa-as.pdf")
