# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from numpy import *

# datos
x=[1,2,3,4,5]
y=[1,4,3,4,5]

fig,eje = plt.subplots(1,1)
eje.plot(x, y, 'ro', label='Datos experimentales')
eje.set_xlabel("$x$")
eje.set_ylabel("$f(x)$")
eje.legend()
eje.set_xlim(0,6)
eje.set_ylim(0,6)
polynomial.
#plt.legend(loc=2) # esquina superior izquierda
#plt.savefig("g1.pdf")
plt.show()