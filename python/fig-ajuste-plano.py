# -*- coding: UTF-8 -*-
from numpy import *
from numpy.linalg import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy.optimize import leastsq

# los datos
x=array([0,2,2.5,1,4,7])
y=array([0,1,2,3,6,2])
z=array([5,10,9,0,3,27])

# Calcula ajuste usando `leastsq` de Scipy

# aquí se definen los *residuos*
def f(a,x,y,z):
    return a[0]+a[1]*x+a[2]*y-z

# parámetros iniciales para el algoritmo
a_in=[1,1,-1]
a,cov=leastsq(f,a_in,args=(x,y,z))

# gráfico de puntos y ajuste
xx=linspace(min(x),max(x),100)
yy=linspace(min(y),max(y),100)
xx,yy=meshgrid(xx,yy) # general una malla con los valores de x e y para el gráfico
zz=a[0]+a[1]*xx+a[2]*yy
fig = figure()
ej = fig.add_subplot(1,1, 1, projection='3d')
ej.plot(x, y, z,'ro')
ej.plot_surface(xx,yy,zz, rstride=100, cstride=100, linewidth=0,alpha=0.2)
ej.view_init(azim=140,elev=20) # define 'perspectiva'
ej.set_xlabel(r'$x$')
ej.set_ylabel(r'$y$')
ej.set_zlabel(r'$z$')
fig.savefig('fig-ajuste-plano.pdf')
#show()

# calcula coeficiente de correlación
su=sum((z-mean(z))**2)
sr=sum((z-(a[0]+a[1]*x+a[2]*y))**2)
r=sqrt((su-sr)/su)

for i in range(3): print('a'+str(i)+' = '+str(a[i]))
print('r = '+str(r))
