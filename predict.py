
with open('model/weights') as f:
	a, b = list(map(float, f.read().split('\n')))

mil = 'init'
while mil != '':
	mil = input("Enter Milleage:")
	