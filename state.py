import chess
import numpy as np

class State():
	def __init__(self, board=None):
		if board is None:
			self.board = chess.Board()
		else:
			self.board = board

	def serialize(self):
		# state = np.zeros((8,8), dtype=np.int8)
		init_state = np.zeros(64, dtype=np.int8)
		state = np.zeros((2,8,8), dtype=np.int8)
		# print(state)

		for idx in range(64):
			symbol = self.board.piece_at(idx)
			if symbol is not None:
				init_state[idx] = {
				"P":1, "N":2, "B":3, "R":4, "Q":5, "K":6,\
				"p":9, "n":10, "b":11, "r":12, "q":13, "k":14}[symbol.symbol()]

		if self.board.ep_square is not None:
			assert init_state[self.board.ep_square] == 0
			init_state[self.board.ep_square] = 7
		if self.board.has_kingside_castling_rights(chess.WHITE):
			assert init_state[7] == 4
			init_state[7] = 8
		if self.board.has_kingside_castling_rights(chess.BLACK):
			assert init_state[63] == 4+8
			init_state[63] = 8+8
		if self.board.has_queenside_castling_rights(chess.WHITE):
			assert init_state[0] == 4
			init_state[0] = 8
		if self.board.has_queenside_castling_rights(chess.BLACK):
			assert init_state[56] == 4+8
			init_state[56] = 8+8

		init_state = np.reshape(init_state, (8,8))
		state[0] = init_state
		state[1] = self.board.turn * 1.0

		print(state.shape)
		print(init_state.shape)
		return state

if __name__ == "__main__":
	s = State()
	s.serialize()
