import torch

class ChessValueDataset(Dataset):
    def __init__(self):
        print("init")
        
data = ChessValueDataset("./process/dataset_10M.npz")
