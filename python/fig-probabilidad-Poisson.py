# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
#from scipy.special import gamma # importa la funcion gamma para calcular factorial
from scipy.stats import poisson # importa la distribucion de Poisson

x=arange(16)

for mu in [1,4,8]:
#	p = exp(-mu)*mu**x/gamma(x+1)  # podemos evaluar directamente la funcion
	p = poisson.pmf(x,mu) # o podemos usar la probabilidad ya definida en scipy.stats
	plot(x,p, marker='o', label=u'$\mu= $'+str(mu))
legend()
grid()
xlabel("$x$")
ylabel("Probabilidad")
savefig("../figs/fig-probabilidad-Poisson.pdf")
