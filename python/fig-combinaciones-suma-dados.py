# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

x=arange(2,13)
y=[1,2,3,4,5,6,5,4,3,2,1]

bar(x,y,align="center")
xlabel("Variable aleatoria, $x$")
ylabel(u"Número de combinaciones")
xlim(0,14)
ylim(0,7)
grid()
savefig("../figs/fig-combinaciones-suma-dados.pdf")
