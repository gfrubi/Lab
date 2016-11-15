# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

# datos
x=[1,2,3,4,5]
y=[1,4,3,4,5]

#crea figura y ejes
scatter(x,y, color='red', label='Datos experimentales') # grafica puntos
xlabel("$x$", fontsize=15)
ylabel("$f(x)$", fontsize=15)
xlim(0,6)
ylim(0,6)
grid()
a = polyfit(x, y, deg=1) # constantes del ajuste lineal. Ojo con el orden!
xx=linspace(0,6,100) 
yy=polyval(a,xx) # evalúa ajuste
plot(xx,yy, color='blue', label='Ajuste') # grafica ajuste
legend(loc='best')
savefig("../figs/fig-mmc.pdf")
