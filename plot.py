import math

import pylab

from matplotlib import mlab

import get_data

data = get_data.get_data()

xlist = [float(s['km']) for s in data]
ylist = [float(s['price']) for s in data]

pylab.plot (xlist, ylist)

pylab.show()