import numpy as np
import csv
import math
import matplotlib.pyplot as plt
import os

from read_data import get_data
from normalize import normalize

# x:  22899.0 240000.0
# y:  3650.0 8290.0

def calc_real_wei(x, y):
	x, y = np.array(x), np.array(y)
	numerator = np.sum((x - np.mean(x)) * (y - np.mean(y)))
	denominator = np.sum((x - np.mean(x)) ** 2)

	a = numerator / denominator
	b = np.mean(y) - (a * np.mean(x))
	return a, b

if __name__ == '__main__':
	os.makedirs('model', exist_ok=True)
	x, y = normalize(*get_data())

	a = 0.
	b = 0.
	n = len(x)
	alpha = 0.001
	num_iter = 200000
	losses = [0. for _ in range(num_iter)]

	for i in range(num_iter):
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
	print("End loss: ", losses[-1])
	print("a, b : ", a, b)
	print("real a, b : ", *calc_real_wei(x, y))
	with open('model/loss', 'w') as f:
		f.write('\n'.join(losses))
	with open('model/weights', 'w') as f:
		f.write(str(a) + '\n' + str(b))