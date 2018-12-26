import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

	def __init__(self):
	  super(Net, self).__init__()
	  # 1 input image channel, 6 output channels, 5x5 square convolution
	  # kernel
	  self.conv1 = nn.Conv2d(1, 6, 5)
	  self.conv2 = nn.Conv2d(6, 16, 5)
	  # an affine operation: y = Wx + b
	  self.fc1 = nn.Linear(16 * 5 * 5, 120)
	  self.fc2 = nn.Linear(120, 84)
	  self.fc3 = nn.Linear(84, 10)

	def forward(self, x):
	  # Max pooling over a (2, 2) window
	  x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
	  # If the size is a square you can only specify a single number
	  x = F.max_pool2d(F.relu(self.conv2(x)), 2)
	  x = x.view(-1, self.num_flat_features(x))
	  x = F.relu(self.fc1(x))
	  x = F.relu(self.fc2(x))
	  x = self.fc3(x)
	  return x

	def load_file(self, file):
		self.data = [ file['arr_0'], file['arr_1'] ]
		# self.data[0] = 
		# self.data[1] = 
		# print(self.data.shape)
		return self.data[0], self.data[1]

	def print_shape(self):
		print(self.data[0].shape, self.data[1].shape)

if __name__ == "__main__":
	# loaded = np.load("proc/dataset.npz")
	net = Net()
	loaded = np.load("proc/dataset.npz")
	datas = net.load_file(loaded)
	# net.print_shape()
	print(net)