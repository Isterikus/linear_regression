import get_data as dt

data = dt.get_data()

samples = 50 # количество точек
packetSize = 5 # размер пакета
gamma = 0.1

def f(km, a, b): return a * km + b # искомая функция

data_x = [[float(km['km']) for km in data[i:i+packetSize]] for i in range(0, len(data), packetSize)]
data_y = [[float(km['price']) for km in data[i:i+packetSize]] for i in range(0, len(data), packetSize)]

a = 0.0 # weight
b = 0.0 # bias

for i in range(len(data_x)):
	sm1 = 0
	sm2 = 0
	# print(data_x[i])
	for j in range(len(data_x[i])):
		# print(km, a, b, data_y[i][j])
		sm1 += f(data_x[i][j], a, b) - data_y[i][j]
		sm2 += (f(data_x[i][j], a, b) - data_y[i][j]) * data_x[i][j]
	print('Loss = ', sm1 / packetSize)
	b = gamma * (sm1 / packetSize)
	a = gamma * (sm2 / packetSize)
	print('a = ', a, ' | b = ', b)