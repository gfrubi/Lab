# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *

# datos
x=[5,20,40,60,80]
y=[2.6,5.0,7.8,11.5,13.9]
errorx=[1,1,1,1,1]
errory=[0.2,0.2,0.2,0.2,0.2]

# Grafica los datos, tamaño 3, 'ro'=círculos rojos
errorbar(x, y, xerr=errorx, yerr=errory, fmt='ro', 
	markersize=3, label='Datos experimentales')
title("Voltaje versus Frecuencia")
xlabel("Frecuencia $f$ [Hertz]")
ylabel("Voltaje $V$ [Volt]")
legend()
grid()
legend(loc=2) # esquina superior izquierda
savefig("../figs/fig-grafico-con-error.pdf")
