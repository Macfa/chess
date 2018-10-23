#!/usr/bin/env python
# coding: utf-8

import chess
import numpy as np

class State(object):
	def __init__(self, board=None):
		if board is None:
			self.board = chess.Board()
		else:
			self.board = board

	# It's position where can i go
	def edge(self):
		return list(self.board.legal_moves)

	# this mean is... data by FEN type maybe.
	def serialize(self):
		# 257 bits according to readme
		assert self.board.is_valid() # what this mean ?
		bstate = np.zeros(64, np.uint8) # fill a 64bit, and its apply a uint8
		for i in range(64): # 64 means chess board
			piece = self.board.piece_at(i) # get a piece ( ex, R, B, N, K, Q, P)
			if piece is not None: # except None
				bstate[i] = {"P":1, "N":2, "B":3, "R":4, "Q":5, "K":6, \
										 "p":9, "n":10, "b":11, "r":12, "q":13, "k":14}[piece.symbol()]
				print(piece)
				pass
		bstate = bstate.reshape(8,8) # gives new shape without changing the data

		state = np.zeros((8,8,5), np.uint8)

		# 0~3 columns to binary
		state[:,:, 0] = (bstate>>3)&1
		state[:,:, 1] = (bstate>>2)&1
		state[:,:, 2] = (bstate>>1)&1
		state[:,:, 3] = (bstate>>0)&1

		# 4th column is who's turn it is
		state[:,:, 4] = (self.board.turn*1.0)
		fen = self.board.shredder_fen()
		return state

	def value(self):
		return 1


if __name__ == "__main__":
  s = State()  # inital class
  print(s.board)
  print(s.edge)
  # print(list(s.board.legal_moves))
  # print("===================")
  # print(s.board.legal_moves)
  # print(s.serialize())

    
