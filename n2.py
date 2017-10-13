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

mean_x = sum(data_x) / float(len(data_x))
mean_y = sum(data_y) / float(len(data_y))

# for i in range(10000):
b_temp_1 = 0
b_temp_2 = 0
for j in range(data_len):
	calc = a * data_x[j] + b
	b_temp_1 += ((data_x[j] - mean_x) * (data_y[j] - mean_y))
	b_temp_2 += pow(data_x[j] - mean_x, 2)
# loss = loss / packetSize
print('s1 = ', b_temp_1)
print('s2 = ', b_temp_2)
a = b_temp_1 / b_temp_2
b = mean_y - b * mean_x
print('a = ', a, ' b = ', b)
for j in range(data_len):
	calc = a * data_x[j] + b
	print('mine = ', calc)
	print('real = ', data_y[j])
	print('--------------------------------------------------')
	# print('diff = ', calc - data_y[j])


	# print('Loss = ', loss)
	# a = a - gamma * (sm2 / packetSize)
	# b = b - gamma * (sm1 / packetSize)

	# if (i % 1000) == 0:
	# 	print("Ошибка после "+str(i)+" повторений:" + str(loss))
		# print('a = ', a, ' | b = ', b)
	# print('Loss = ', loss)