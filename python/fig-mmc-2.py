# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *
from scipy.optimize import curve_fit

# datos
x=array([0.1, 0.25, 0.41, 0.56, 0.71, 0.86, 1.02, 1.17, 1.32, 1.47, 1.63, 1.78, 
	1.93, 2.08, 2.24, 2.39, 2.54, 2.69, 2.85, 3.])
y=array([0.738, 0.826, 0.981, 0.974, 0.915, 0.897, 0.739, 0.785, 0.635, 0.520, 
	0.490, 0.428, 0.497, 0.355, 0.359, 0.328, 0.440, 0.441, 0.433, 0.419])

def f(x,a,b,c):
    return a+exp(-b*x)*sin(c*x)
(a,b,c), _=curve_fit(f,x,y)

xx=linspace(0,3.1,200)
plot(x,y,'ro', label='Datos experimentales')
plot(xx,f(xx,a,b,c),label='Ajuste')
xlabel("$x$")
ylabel("$y$")
xlim(0,3.1)
ylim(0,1.2)
legend()

savefig('fig-mmc-2.pdf')
