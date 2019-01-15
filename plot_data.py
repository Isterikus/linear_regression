import matplotlib.pyplot as plt
import csv
import sys

from read_data import get_data
from normalize import normalize

x, y = get_data()

try:
	if len(sys.argv) > 1:
		x, y = normalize(x, y)
except:
	print("Train first")
	exit()

fig, ax = plt.subplots(figsize = (12, 8))
ax.scatter(x, y, label = 'Traning Data')
ax.legend(loc = 2)
ax.set_xlabel('Milleage')
ax.set_ylabel('Price')
ax.set_title('Price vs. Milleage')
plt.show()