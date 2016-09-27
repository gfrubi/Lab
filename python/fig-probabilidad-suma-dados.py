# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

x=arange(2,13)
y=array([1,2,3,4,5,6,5,4,3,2,1])

bar(x,y/float(sum(y)),align="center")
xlabel("Variable aleatoria, $x$")
ylabel(u"Probabilidad")
xlim(0,14)
grid()
savefig("../figs/fig-probabilidad-suma-dados.pdf")
