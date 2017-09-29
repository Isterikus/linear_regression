import get_data as dt

data = dt.get_data()

samples = 50 # количество точек
packetSize = 24 # размер пакета
gamma = 0.5
data_len = len(data)
# gamma = 10

def f(km, a, b): return a * km + b # искомая функция

data_x = [float(s['km']) for s in data]
data_y = [float(s['price']) for s in data]

a = -0.00838 # weight
b = 5661.17 # bias
# a = 0.0
# b = 0.0

for i in range(10000):
	sm1 = 0.0
	sm2 = 0.0
	loss = 0.0
	for j in range(data_len):
		calc = a * data_x[j] + b
		diff = calc - data_y[j]
		loss += pow(diff, 2)
		sm1 += (diff) * 2
		sm2 += (diff) * data_x[j] * 2
	loss = loss / packetSize
	# print('Loss = ', loss)
	a = a - gamma * (sm2 / packetSize)
	b = b - gamma * (sm1 / packetSize)

	if (i % 1000) == 0:
		print("Ошибка после "+str(i)+" повторений:" + str(loss))
		# print('a = ', a, ' | b = ', b)
	# print('Loss = ', loss)