# -*- coding: UTF-8 -*-
# adaptado a partir de la figura en http://en.wikipedia.org/wiki/File:Normal_Distribution_PDF.svg
from numpy import *
import matplotlib.pyplot as p

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*pi)**.5) * e ** (-(x-mu)**2/(2 * sig**2))

x = arange(-7, 7, 0.01)
s = [1.,3.] # sigma's
m = [0., 0.] # mu's
c = ['b','r'] # colores

for sig, mu, color in zip(s, m, c): 
        gauss = make_gauss(1, sig, mu)(x)
        plot(x, gauss, color, linewidth=2)
        bar(0,make_gauss(1,sig,0)(sig), width=sig*1.99, align="center",alpha=0.2, color=color)

xlim(-7, 7)
ylim(0, .45)
legend([r'$\sigma=$'+str(s[0]), r'$\sigma=$'+str(s[1])], loc='best')
xlabel('$x$')
ylabel('$f(x)$')
grid(True)
savefig('fig-normal.pdf')
