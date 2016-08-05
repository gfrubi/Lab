# -*- coding: utf-8 -*-
from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import leastsq

x=array([1,2,3,4,5,6])
y=array([2.8,3.3,3.5,3.5,4.8,4.2])
ey=array([0.3,0.3,0.5,1.0,0.3,1])

# residuos a minimizar
def f(a,x,y,ey):
    return (a[0]+a[1]*x-y)/ey
    
a_in=[1,1] # valor inicial
aes,cov=leastsq(f,a_in,args=(x,y,ey))

# grafica
errorbar(x,y,ey,fmt='o')
xx=linspace(min(x),max(x),100)
plot(xx,polyval(polyfit(x,y,1),xx), label='MC no ponderado',lw=1.5)
plot(xx,f(aes,xx,0,1),label='MC ponderado',lw=1.5)
xlim(0,7)
ylim(0,7)
grid()
legend(loc='best')
title(u'Ajuste por Mínimos Cuadrados (MC)')
xlabel(r'$x$')
ylabel(r'$y$')
savefig('fig-mc-ponderado.pdf')
