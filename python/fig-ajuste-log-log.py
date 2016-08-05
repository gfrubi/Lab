# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

# datos
x=[5,16,80,160,400]
y=[1,2,4,6,9.8]
errorx=[0.3,1,1,5,5]
errory=[0.2,0.2,0.2,0.2,0.2]

# Grafica los datos, tamaño 3, 'ro'=círculos rojos
errorbar(x, y, xerr=errorx, yerr=errory, fmt='ro', 
	markersize=3, label='Datos experimentales')
# Grafica ajute
xa=linspace(1,450,100)
ya=0.46*xa**0.5
#plot(xa,ya, label='Ajuste')
loglog(xa,ya, basex=10, basey=10, label='Ajuste')
title(u"Fuerza versus Deformación")
xlabel("Fuerza $F$ [N]")
ylabel(u"Deformación $L$ [mm]")
legend()
legend(loc=2) # esquina superior izquierda
savefig("fig-ajuste-log-log.pdf")
