import numpy as np
import csv
import math
import matplotlib.pyplot as plt
import os

from read_data import get_data

# x:  22899.0 240000.0
# y:  3650.0 8290.0

def normilize(x, y):
	mn = min(x)
	mx = max(x)
	print('x: ', mn, mx)
	x = [(s - mn) / (mx - mn) for s in x]
	mn = min(y)
	mx = max(y)
	print('y: ', mn, mx)
	y = [(s - mn) / (mx - mn) for s in y]
	return x, y

def new_norm(x, y):
	m = np.mean(x)
	s = np.sqrt(np.sum(np.power(x - m, 2)) / len(x))
	print(m, s)
	x = [(v - m) / s for v in x]
	m = np.mean(y)
	s = np.sqrt(np.sum(np.power(y - m, 2)) / len(y))
	print(m, s)
	y = [(v - m) / s for v in y]
	return x, y

if __name__ == '__main__':
	# x, y = normilize(*get_data())
	# x, y = new_norm(*get_data())
	x, y = get_data()

	a = 0.
	b = 0.
	n = len(x)
	alpha = 0.000001
	num_iter = 7000
	losses = [0. for _ in range(num_iter)]

	for i in range(num_iter):
		print(i)
		sm1 = 0.
		sm2 = 0.
		for j in range(n):
			calc = a * x[j] + b
			diff = calc - y[j]
			losses[i] += pow(diff, 2)
			sm1 += (diff) * 2
			sm2 += (diff) * x[j] * 2
		losses[i] = str(losses[i] / n)
		a = a - alpha * (sm2 / n)
		b = b - alpha * (sm1 / n)
	print(a, b)
	os.makedirs('model', exist_ok=True)
	with open('model/loss', 'w') as f:
		f.write('\n'.join(losses))
	with open('model/weights_norm', 'w') as f:
		f.write(str(a) + '\n' + str(b))
	with open('model/weights', 'w') as f:
		f.write(str(a) + '\n' + str(b * 8290.))