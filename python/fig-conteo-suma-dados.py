# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

xa=arange(2,13)
na=array([2703,5526,8320,11205,13685,16778,13870,11173,8517,5511,2712])

bar(xa,na,align="center")
xlabel("Valores variable aleatoria, $x$")
ylabel(u"Número de ocurrencias")
xlim(0,14)
grid()
savefig("../figs/fig-barras-dados-1E5.pdf")
