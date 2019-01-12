import csv

def get_data():
	with open("data/cars.csv") as f:
		data = list(csv.reader(f))
		del data[0]

	x = [float(s[0]) for s in data]
	y = [float(s[1]) for s in data]
	return x, y