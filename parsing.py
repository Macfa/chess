import chess.pgn
import os

file_list = os.listdir('./data')

for file in file_list:
	pgn = open(os.path.join("./data", file))
	# print(os.path.join("./data/", file))
	game = chess.pgn.read_game(pgn)

	# # Iterate through all moves and play them on a board.
	board = game.board()
	print(board)
	# for move in :
	# 	board.push(move)
	
	# print(game)
	
# first_game.headers["Event"]


