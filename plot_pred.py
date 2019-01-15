import matplotlib.pyplot as plt

from normalize import normalize
from read_data import get_data
from train import calc_real_wei

try:
	with open('model/weights') as f:
		a, b = list(map(float, f.read().split('\n')))
except:
	print("Train first")
	exit()

x, y = normalize(*get_data())
real_a, real_b = calc_real_wei(x, y)

pred = [a * el + b for el in x]
real_pred = [real_a * el + real_b for el in x]

fig, ax = plt.subplots(figsize = (12, 8))
ax.plot(x, pred, 'r', label = 'Prediction')
ax.plot(x, real_pred, 'b', label = 'Real line')
ax.scatter(x, y, label = 'Traning Data')
ax.legend(loc = 2)
ax.set_xlabel('Milleage')
ax.set_ylabel('Price')
ax.set_title('Predicted price vs. milleage')
plt.show()