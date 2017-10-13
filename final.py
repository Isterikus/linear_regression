import numpy
import csv
import math

import pylab

from matplotlib import mlab
import matplotlib.pyplot as plt

data = []
with open("data/cars.csv") as f:
	data = list(csv.reader(f))
	del data[0]

x = [float(s[0]) for s in data]
y = [float(s[1]) for s in data]

def normilize():
	global x,y
	mn = min(x)
	mx = max(x)
	print()
	x = [(s - mn) / (mx - mn) for s in x]
	mn = min(y)
	mx = max(y)
	y = [(s - mn) / (mx - mn) for s in y]

normilize()

a = 0
b = 0
packetSize = len(x)
gamma = 0.01
for i in range(10000):
	sm1 = 0.0
	sm2 = 0.0
	loss = 0.0
	for j in range(len(x)):
		calc = a * x[j] + b
		diff = calc - y[j]
		loss += pow(diff, 2)
		sm1 += (diff) * 2
		sm2 += (diff) * x[j] * 2
	loss = loss / packetSize
	# print('Loss = ', loss)
	a = a - gamma * (sm2 / packetSize)
	b = b - gamma * (sm1 / packetSize)

	if (i % 1000) == 0:
		print("Ошибка после "+str(i)+" повторений:" + str(loss))

print(a)
print(b)

pred = []
for el in x:
	pred.append(a * el + b)
# pylab.plot (x, y)

# pylab.show()


fig, ax = plt.subplots(figsize = (12, 8))
ax.plot(x, pred, 'r', label = 'Prediction')
ax.scatter(x, y, label = 'Traning Data')
ax.legend(loc = 2)
ax.set_xlabel('Milleage')
ax.set_ylabel('Price')
ax.set_title('Predicted price vs. milleage')
plt.show()