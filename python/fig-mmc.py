# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

# datos
x=[1,2,3,4,5]
y=[1,4,3,4,5]

#crea figura y ejes
plot(x, y, 'ro', label='Datos experimentales') # grafica puntos
xlabel("$x$")
ylabel("$f(x)$")
xlim(0,6)
ylim(0,6)
a1,a0= polyfit(x, y, deg=1) # constantes del ajuste lineal. Ojo con el orden!
xx=linspace(0,6,100) 
yy=a0+a1*xx # evalúa ajuste
plot(xx,yy,'-b', label='Ajuste') # grafica ajuste
legend(loc=2)
savefig("fig-mmc.pdf")
