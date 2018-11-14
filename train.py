import numpy as np
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torch
import torch.optim as optim

class CustomDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self):
        loaded = np.load("process/dataset_2M.npz")
        self.X = loaded["arr_0"]
        self.Y = loaded["arr_1"]
        print("Loaded ", self.X.shape, self.Y.shape)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.Y[idx]
        # pass
    # Loaded  (20055, 5, 8, 8) (20055,)


class Net(nn.Module):
    # (in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True)
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(8, 8, kernel_size=1)
        self.conv2 = nn.Conv2d(8, 8, kernel_size=1)
        self.conv3 = nn.Conv2d(8, 8, kernel_size=1)
        self.conv4 = nn.Conv2d(8, 8, kernel_size=1)
        self.fc1 = nn.Linear(8 * 8 * 5, 8)
        self.fc2 = nn.Linear(8 * 8 * 5, 8 * 2)
        self.fc3 = nn.Linear(8 * 8 * 5, 8 * 3)
        self.fc4 = nn.Linear(8 * 8 * 5, 8 * 4)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

if __name__ == "__main__":
    custom = CustomDataset()
    net = Net()
    train_dataset = torch.utils.data.DataLoader(custom, batch_size=5)

    for i in train_dataset:
        print(i)

    # Define a Loss function and optimizer
    loss = nn.CrossEntropyLoss()

    # criterion = nn.CrossEntropyLoss()
    # optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)


    # Train the Network
    
# for epoch in range(2):  # loop over the dataset multiple times

#     running_loss = 0.0
#     for i, data in enumerate(trainloader, 0):
#         # get the inputs
#         inputs, labels = data

#         # zero the parameter gradients
#         optimizer.zero_grad()

#         # forward + backward + optimize
#         outputs = net(inputs)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()

#         # print statistics
#         running_loss += loss.item()
#         if i % 2000 == 1999:    # print every 2000 mini-batches
#             print('[%d, %5d] loss: %.3f' %
#                   (epoch + 1, i + 1, running_loss / 2000))
#             running_loss = 0.0

# print('Finished Training')
