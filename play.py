import numpy as np

if __name__ == "__main__":
	opened = open("proc/dataset.npz",'rb')
	print(opened)
	np.load(opened)
	# loaded = np.load("proc/dataset.npz")
	# print(loaded)
