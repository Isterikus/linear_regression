import math
#Импортируем один из пакетов Matplotlib
import pylab
#Импортируем пакет со вспомогательными функциями
from matplotlib import mlab

import get_data

data = get_data.get_data()

xlist = [float(s['km']) for s in data]
ylist = [float(s['price']) for s in data]

#Нарисуем одномерный график
pylab.plot (xlist, ylist)

#Покажем окно с нарисованным графиком
pylab.show()