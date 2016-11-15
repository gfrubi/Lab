# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
# datos
x=[1,2,3,4,5]
y=[1,4,3,4,5]

scatter(x, y, color='red', label='Datos experimentales') # grafica datos
plot(x, y, '--b', label=u'Interpolación lineal') # grafica lineas entre puntos
xlabel("$x$", fontsize=15)
ylabel("$f(x)$", fontsize=15)
xlim(0,6)
ylim(0,6)
legend(loc='best')
grid()
savefig("../figs/fig-int-lineal.pdf")
