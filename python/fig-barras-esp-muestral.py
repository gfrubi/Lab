# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

x=xrange(2,13)
y=[1,2,3,4,5,6,5,4,3,2,1]

bar(x,y,align="center")
xlabel("Variable aleatoria, $x$")
ylabel(u"Número de combinaciones")
xlim([0,14])
grid()
savefig("fig-barras-esp-muestral.pdf")
