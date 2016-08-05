# -*- coding: UTF -8 -*-
from matplotlib.pyplot import *
from numpy import *

x=linspace(0,30,200)
y=1000*exp(-(x-13)**2/15)

# crea figura y eje
plot(x, y, lw=2)
xlabel(u'Energía, $x$ (eV)')
ylabel(u"Número de ocurrencias")
#eje.set_xlim(0,6)
ylim(0,1200)
grid(True)

savefig("fig-Gauss.pdf")
