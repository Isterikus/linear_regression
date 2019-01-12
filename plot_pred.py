import matplotlib.pyplot as plt
from train import normilize
from read_data import get_data

with open('model/weights') as f:
	a, b = list(map(float, f.read().split('\n')))

# x, y = normilize(*get_data())
x, y = get_data()

pred = []
for el in x:
	print(a * el + b)
	pred.append(a * el + b)

fig, ax = plt.subplots(figsize = (12, 8))
ax.plot(x, pred, 'r', label = 'Prediction')
ax.scatter(x, y, label = 'Traning Data')
ax.legend(loc = 2)
ax.set_xlabel('Milleage')
ax.set_ylabel('Price')
ax.set_title('Predicted price vs. milleage')
plt.show()