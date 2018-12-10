import chess.pgn
import os
import numpy as np
from state import State

def generate_dataset(dataset_limit=None):
    X,Y = [], []
    has_played = 1
    datas = os.listdir("data")
    res_type = { "0-1": -1, "1/2-1/2":0, "1-0":1 }

    for data in datas:
        pgn = open(os.path.join("data", data))
        while(1):   # below content get a indent
            game = chess.pgn.read_game(pgn)

            if game is None:
                break
            # print(game)

            board = game.board()
            res = game.headers["Result"]

            if res in res_type:
                res = res_type[res]

            for move in game.main_line():
                board.push(move)
                ser = State(board).serialize()
                # print(ser)
                X.append(ser)
                Y.append(res)
            print("Parsing %d Games, %d Examples has done" % (has_played, len(X)))
            if dataset_limit is None or len(X) > dataset_limit:
                return X,Y
            has_played += 1
    return X,Y

if __name__ == "__main__":
    X,Y = generate_dataset(25000)
    np.savez_compressed("process/dataset_2M", X, Y)
