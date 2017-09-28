import csv
data_path = "./data/cars.csv"

def get_data():
	with open(data_path) as f:
		data = list(csv.DictReader(f))
	return data