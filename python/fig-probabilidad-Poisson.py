# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
from scipy.special import gamma

datbabs = genfromtxt("datos_poisson.txt")
x=datbabs[:,0]
y=datbabs[:,1]

p=y/sum(y) # probabilidad 
mu=sum(x*p) # mu calculado como el valor medio

xx=linspace(0,12,100)
poisson=exp(-mu)*mu**xx/gamma(xx+1)

bar(x,p,align="center")
plot(xx,poisson, 'r', linewidth=2)
xlabel("Variable independiente")
ylabel(u"Probabilidad")
xlim([-.6,12])
eje.set_xlim([-.6,12])
fig.savefig("fig-probabilidad-Poisson.pdf")
