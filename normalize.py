import numpy as np

# Possible values: 'min_max', 'mean', 'standart'
norm = 'mean'

# https://en.wikipedia.org/wiki/Standard_deviation
# Делим на длину - 1 потому что имеем не полную выборку
def calc_mean_standart_derivation(point):
	m = np.mean(point)
	s = np.sqrt(np.sum(np.power(point - m, 2)) / (len(point) - 1))
	return m, s


# https://en.wikipedia.org/wiki/Feature_scaling
def min_max_norm_one(val, mn, mx):
	return (val - mn) / (mx - mn)


def mean_norm_one(val, mn, mean, mx):
	return (val - mn) / (mx - mn)


def standart_score_one(val, m, s):
	return (v - m) / s


def min_max_norm(x, y):
	mn, mx = min(x), max(x)
	with open('model/additional_x', 'w') as f:
		f.write(str(mn) + '\n' + str(mx))
	x = [min_max_norm_one(s, mn, mx) for s in x]
	mn, mx = min(y), max(y)
	with open('model/additional_y', 'w') as f:
		f.write(str(mn) + '\n' + str(mx))
	y = [min_max_norm_one(s, mn, mx) for s in y]
	return x, y


def mean_norm(x, y):
	mn, m, mx = min(x), np.mean(x), max(x)
	with open('model/additional_x', 'w') as f:
		f.write(str(mn) + '\n' + str(m) + '\n' + str(mx))
	x = [mean_norm_one(s, mn, m, mx) for s in x]
	mn, m, mx = min(y), np.mean(y), max(y)
	with open('model/additional_y', 'w') as f:
		f.write(str(mn) + '\n' + str(m) + '\n' + str(mx))
	y = [mean_norm_one(s, mn, m, mx) for s in y]
	return x, y


# https://en.wikipedia.org/wiki/Standard_score
def standart_score(x, y):
	m, s = calc_standart_derivation(x)
	with open('model/additional_x', 'w') as f:
		f.write(str(m) + '\n' + str(s))
	x = [standart_score_one(v, m, s) for v in x]
	m, s = calc_standart_derivation(y)
	with open('model/additional_y', 'w') as f:
		f.write(str(m) + '\n' + str(s))
	y = [standart_score_one(v, m, s) for v in y]
	return x, y


def d_min_max_norm(y):
	with open('model/additional_y') as f:
		mn_y, mx_y = list(map(float, f.read().split('\n')))
	return y * (mx_y - mn_y) + mn_y


def d_mean_norm(y):
	with open('model/additional_y') as f:
		mn_y, mean_y, mx_y = list(map(float, f.read().split('\n')))
	return y * (mx_y - mn_y) + mean_y


def d_standart_score(y):
	with open('model/additional_y') as f:
		m, s = list(map(float, f.read().split('\n')))
	return s * y + m


if norm == 'mean':
	normalize_pred_x = mean_norm_one
	normalize = mean_norm
	denormalize = d_mean_norm
elif norm == 'standart':
	normalize_pred_x = standart_score_one
	normalize = standart_score
	denormalize = d_standart_score
else:
	normalize_pred_x = min_max_norm_one
	normalize = min_max_norm
	denormalize = d_min_max_norm
