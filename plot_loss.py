import matplotlib.pyplot as plt

try:
	with open('model/loss') as f:
		losses = list(map(float, f.read().split('\n')))
except:
	print("Train first")
	exit()

fig, ax = plt.subplots(figsize = (12, 8))
ax.plot(list(range(len(losses))), losses, 'r')
ax.legend(loc = 2)
ax.set_xlabel('Iterations')
ax.set_ylabel('Loss')
ax.set_title('Loss function')
plt.show()