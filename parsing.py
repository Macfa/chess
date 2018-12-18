import chess.pgn
import os
import numpy as np
from state import State

def save_data(data_limit=None):
	file_list = os.listdir('./data')
	score = 0
	res_type = {'1-0':-1, '1/2-1/2':0, '0-1':1}
	X,Y = [],[]

	for file in file_list:
		pgn = open(os.path.join("./data", file))
		while 1:
			game = chess.pgn.read_game(pgn)
			if game is None:
				break
			res = game.headers['Result']
			if res not in res_type:
				continue
			
			res = res_type[res]
			score += 1
			board = game.board()

			for move in game.main_line():
				board.push(move)
				X.append(State(board).serialize())
				Y.append(res)
			print("%d Game, %d parsing" % (score, len(X)))
			if data_limit is not None and len(X) > data_limit:
				return X,Y


if __name__ == "__main__":
	# X,Y = save_data(300)
	X,Y = save_data(300000)
	# print(X,Y)
	# np.save('./proc/dataset', (X,Y))
	np.savez('./proc/dataset', (X,Y))
