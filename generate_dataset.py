import os
import chess
import chess.pgn

class get_dataset():
# class get_dataset(read_num=10000):
    idx = 0
    chess = chess
    lists = os.listdir("data")
    for i in lists:
        games = open(os.path.join("./data/", i), 'r')
        game = chess.pgn.read_game(games)
        board = game.board()
#         print(game.headers['Result'])
        for j, move in enumerate(game.main_line()):
            print(idx, move)
            board.push(move)
        idx += 1
        
        
get = get_dataset()

