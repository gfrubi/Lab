# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

datbabs = genfromtxt("datos_poisson.txt")
x=datbabs[:,0]
n=datbabs[:,1]
bar(x,n,align="center")
xlabel("Variable aleatoria, $x$")
ylabel(u"Número de ocurrencias")
xlim([-.6,12])
grid()
savefig("../figs/fig-Poisson.pdf")
