# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

datbabs = genfromtxt("datos_poisson.txt")
x=datbabs[:,0]
y=datbabs[:,1]
bar(x,y,align="center")
xlabel("Valor de variable aleatoria, $x$")
ylabel(u"Número de ocurrencias")
xlim([-.6,12])
grid()
savefig("fig-Poisson.pdf")
