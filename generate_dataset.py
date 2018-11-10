import os
import chess.pgn
import numpy as np
from state import State

def get_dataset(read_num=None):
    idx = 0
    values = {'1/2-1/2':0, '0-1':-1, '1-0':1}
    X,Y = [],[]
    lists = os.listdir("data")
    for i in lists:
        games = open(os.path.join("./data/", i), 'r')
        while 1:
            game = chess.pgn.read_game(games)
            if game is None:
                break
            result = game.headers["Result"]
            if result not in values:
                continue
            result = values[result]
            board = game.board()
            
            for j, move in enumerate(game.main_line()):
                ser = State(board).serialize()
                board.push(move)
                X.append(ser)
                Y.append(move)
            print("Parsing Game : %d, got %d Examples" % (idx, len(X)))
            if read_num is not None and len(X) > read_num:
                return X,Y
            idx += 1
    X = np.array(X)
    Y = np.array(Y)
    return X,Y
        
if __name__ == "__main__":
    X,Y = get_dataset(1000)
    np.savez("./process/dataset_1M.npz", X, Y)
