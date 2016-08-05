# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

# datos
x=[5,20,40,60,80]
y=[2.6,5.0,7.8,11.5,13.9]
errorx=[1,1,1,1,1]
errory=[0.2,0.2,0.2,0.2,0.2]

# Grafica los datos, tamaño 3, 'ro'=círculos rojos
errorbar(x, y, xerr=errorx, yerr=errory, fmt='ro', 
	markersize=3, label='Datos experimentales')
# Grafica ajute
xa=linspace(0,90,100)
ya=0.15*xa+2.0
plot(xa,ya, label='Ajuste')
title("Voltaje versus Frecuencia")
xlabel("Frecuencia $f$ [Hertz]")
ylabel("Voltaje $V$ [Volt]")
legend()
grid()
legend(loc=2) # esquina superior izquierda
savefig("../figs/fig-ajuste-lineal.pdf")
