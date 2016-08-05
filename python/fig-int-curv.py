# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
# datos
x=[1,2,3,4,5]
y=[1,4,3,4,5]

# crea figura y eje
plot(x, y, 'ro', label='Datos experimentales') # grafica datos

xlabel("$x$")
ylabel("$f(x)$")
xlim(0,6)
ylim(0,6)

aes= polyfit(x, y, deg=4) # asigna constantes de ajuste con polinomio grado 4

xx=linspace(min(x),max(x),100)
yy=polyval(aes,xx) # evalúa polinimio con ctes aes, usando función polyval

plot(xx,yy,'-b', label='Ajuste') # grafica ajuste
legend(loc=2)

savefig("fig-int-curv.pdf")
