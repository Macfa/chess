import numpy as np
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torch
import torch.optim as optim
import torch.nn.functional as F


class CustomDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self):
        loaded = np.load("process/dataset_2M.npz")
        self.X = loaded["arr_0"]
        self.Y = loaded["arr_1"]
        print("Loaded ", self.X.shape, self.Y.shape)
        # print(self.X)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.Y[idx]
        # pass
    # Loaded  (20055, 5, 8, 8) (20055,) <-- DataSet Size
    # Loaded  (15030, 5, 8, 8) (15030,)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # (in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True)
        self.a1 = nn.Conv2d(5, 16, kernel_size=3, padding=1)
        self.a2 = nn.Conv2d(16, 16, kernel_size=3, padding=1)
        self.a3 = nn.Conv2d(16, 16, kernel_size=3)

        self.b1 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.b2 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.b3 = nn.Conv2d(32, 32, kernel_size=3)

        self.c1 = nn.Conv2d(32, 64, kernel_size=2, padding=1)
        self.c2 = nn.Conv2d(64, 64, kernel_size=2, padding=1)
        self.c3 = nn.Conv2d(64, 64, kernel_size=2)

        self.d1 = nn.Conv2d(64, 128, kernel_size=3)
        self.d2 = nn.Conv2d(128, 128, kernel_size=2)
        self.d3 = nn.Conv2d(128, 128, kernel_size=2, stride=2)

        self.last = nn.Linear(128, 1)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        x = F.relu(self.a1(x))
        x = F.relu(self.a2(x))
        x = F.relu(self.a3(x))
        # x = F.max_pool2d(x, 2)

        # 4x4
        x = F.relu(self.b1(x))
        x = F.relu(self.b2(x))
        x = F.relu(self.b3(x))
        # x = F.max_pool2d(x, 2)

        # 2x2
        x = F.relu(self.c1(x))
        x = F.relu(self.c2(x))
        x = F.relu(self.c3(x))
        # x = F.max_pool2d(x, 2)

        # 1x128
        x = F.relu(self.d1(x))
        x = F.relu(self.d2(x))
        x = F.relu(self.d3(x))
        # x = F.max_pool2d(x, 2)

        x = x.view(-1, 128)
        x = self.last(x)
        # x = x.view(-1, 128)
        # x = x.view(1, -1)
        return F.sigmoid(x)


if __name__ == "__main__":

    # Device configuration
    device = 'cpu'

    # DataSet Loading & and how many load on way & made it could be iterable
    custom = CustomDataset()
    train_dataset = torch.utils.data.DataLoader(custom, batch_size=256)

    # define model
    model = Net()

    # Define a Loss function and optimizer
    optimizer = torch.optim.Adam(model.parameters())
    mseloss = nn.MSELoss()

    # Train the model
    model.train()

    total_step = len(train_dataset)

    for epoch in range(2):
        all_loss, num_loss = 0, 0;
        for batch, (data, labels) in enumerate(train_dataset):
            labels = labels.unsqueeze(-1)

            # labels = labels.unsqueeze(0)
            data = data.float()
            labels = labels.float()
            optimizer.zero_grad()

            # Forward pass
            outputs = model(data)
            loss = mseloss(outputs, labels)

            # Backward and optimize
            loss.backward()
            optimizer.step()

            all_loss += loss.item()
            num_loss += 1
            print("%3d game loaded : %f" % (batch, all_loss/num_loss))

    print("%3d : %f" % (epoch, all_loss/num_loss))
    torch.save(model.state_dict(), "nets/value.pth")

        # if (i+1) % 100 == 0:
            # print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
                   # .format(epoch+1, 1, i+1, total_step, loss.item()))



    print('%d Finished Training' % total_step)
