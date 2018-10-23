#!/usr/bin/env python
# coding: utf-8

import os
import chess.pgn
from State import *

for files in os.listdir("cct"):
	print(files)
	pgn = open(os.path.join("cct", files))
	while 1:
		try:
			game = chess.pgn.read_game(pgn)
		except Exception:
			break
		result = {'1/2-1/2':0, '0-1':-1, '1-0':1}[game.headers['Result']]
		board = game.board()
		for i, move in enumerate(game.main_line()):
			board.push(move)
			print(result, State(board).serialize())
		exit(0)
	break
