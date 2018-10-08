# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

datbabs = genfromtxt("datos-ba-bs.txt")
x=datbabs[:,0]
y=datbabs[:,1]
bar(x,y,align="center")
xlabel("Variable aleatoria")
ylabel("Número de ocurrencias")
title("a) Bajo error aleatorio, bajo error sistemático")
xlim(0,20)
ylim(0,16)
savefig("fig-ba-bs.pdf")
