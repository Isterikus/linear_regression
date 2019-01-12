import matplotlib.pyplot as plt
import csv

with open("data/cars.csv") as f:
	data = list(csv.reader(f))
	del data[0]

x = [float(s[0]) for s in data]
y = [float(s[1]) for s in data]

fig, ax = plt.subplots(figsize = (12, 8))
# ax.plot(x, pred, 'r', label = 'Prediction')
ax.scatter(x, y, label = 'Traning Data')
ax.legend(loc = 2)
ax.set_xlabel('Milleage')
ax.set_ylabel('Price')
ax.set_title('Price vs. Milleage')
plt.show()