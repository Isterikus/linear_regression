import os

from train import calc_real_wei
from normalize import normalize_pred_x, denormalize, normalize
from read_data import get_data

if not os.path.isfile('model/weights'):
	print("Train first")
	exit()

with open('model/weights') as f:
	a, b = list(map(float, f.read().split('\n')))

real_norm_a, real_norm_b = calc_real_wei(*normalize(*get_data()))
real_a, real_b = calc_real_wei(*get_data())

mil = 'init'

with open('model/additional_x') as f:
	additional = list(map(float, f.read().split('\n')))

while True:
	try:
		mil = float(input("Enter Milleage:"))
	except:
		print("Not float input, exiting")
		exit()

	try:
		mil_n = normalize_pred_x(mil, *additional)
	except:
		print("Retrain with suggested normalize!")
		exit()

	pred = a * mil_n + b
	real_norm_pred = real_norm_a * mil_n + real_norm_b
	real_pred = real_a * mil + real_b

	pred_d = denormalize(pred)
	real_norm_pred_d = denormalize(real_norm_pred)
	print("Predict : ", pred_d)
	print("Predict real normalized : ", real_norm_pred_d)
	print("Error real normalized : ", abs(real_norm_pred_d - pred_d))
	print("Predict real : ", real_pred)
	print("Error real : ", abs(real_pred - pred_d))
