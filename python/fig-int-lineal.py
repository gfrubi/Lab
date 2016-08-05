# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
# datos
x=[1,2,3,4,5]
y=[1,4,3,4,5]

plot(x, y, 'or', label='Datos experimentales') # grafica datos
plot(x, y, '--b', label='Ajuste') # grafica lineas entre puntos
xlabel("$x$")
ylabel("$f(x)$")
xlim(0,6)
ylim(0,6)
legend(loc=2)

savefig("fig-int-lineal.pdf")
