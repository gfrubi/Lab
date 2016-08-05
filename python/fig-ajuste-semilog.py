# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

# datos
x=[4,8,16,20,24]
y=[0.780,0.260,0.040,0.015,0.005]
errorx=[0.1,0.1,0.1,0.1,0.1]
errory=[0.002,0.002,0.002,0.002,0.002]

# Grafica los datos, tamaño 3, 'ro'=círculos rojos
errorbar(x, y, xerr=errorx, yerr=errory, fmt='ro', 
	markersize=3, label='Datos experimentales')
# Grafica ajuste
xa=linspace(3,25,100)
ya=2.0*exp(-xa/1000/0.004)
#plot(xa,ya, label='Ajuste')
semilogy(xa,ya, basey=10, label='Ajuste')
title(u"Carga eléctrica versus Tiempo")
xlabel("Tiempo $t$ [ms]")
ylabel(u"Carga eléctrica $Q$ [mC]")
legend()
legend(loc=1) # esquina superior derecha
savefig("fig-ajuste-semilog.pdf")
