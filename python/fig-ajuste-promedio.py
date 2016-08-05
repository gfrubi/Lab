# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

t1=[122,132,122,130,131,109,110,127,127,117,120] # datos experimentales
num1=range(1,len(t1)+1) # genera número de la medida a partir de t1

print('promedio ='), mean(t1)

plot(num1, t1, 'bo',label=u'Datos Experimentales')
axhline(y=mean(t1), xmin=0, xmax=len(t1),color='r', label='Promedio') # linea horizontal en promedio 1
xlabel(u'Número de la medida')
ylabel(u'Tiempo $t$ [s]')
ylim(0,200)
legend(loc='best')
savefig('fig-ajuste-promedio.pdf')
