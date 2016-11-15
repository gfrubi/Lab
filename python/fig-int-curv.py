# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
# datos
x=[1,2,3,4,5]
y=[1,4,3,4,5]

# crea figura y eje
scatter(x, y, color='red', label='Datos experimentales') # grafica datos
xlabel("$x$", fontsize=15)
ylabel("$f(x)$", fontsize=15)
xlim(0,6)
ylim(0,6)

from scipy.interpolate import UnivariateSpline
s = UnivariateSpline(x, y, s=0) # interpolación usando spline cúbica

xx=linspace(min(x),max(x),100)
yy=s(xx) # evalúa polinomio con ctes. a, usando función polyval

plot(xx,yy,'-b', label=u'Spline cúbica') # grafica ajuste
legend(loc='best')
grid()
savefig("../figs/fig-int-curv.pdf")
