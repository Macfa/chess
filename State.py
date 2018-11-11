import chess
import numpy as np


class state():
    def __init__(self, board=None):
        if board is not None:
            self.board = board
        else:
            self.board = chess.Board()

    def list(self):
        return self.board.pseudo_legal_moves

    def clean(self):
        return self.board.clear()

    def initialize(self):
        state = np.zeros((8,8))
        init_piece = np.zeros(64, int)

        for idx in range(64):
            symbol = self.board.piece_at(idx)

            if symbol is not None:
                init_piece[idx] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                 "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[symbol.symbol()]


            if self.board.has_kingside_castling_rights(chess.WHITE):
                init_piece[0] = 7

            if self.board.has_kingside_castling_rights(chess.BLACK):
                init_piece[63] = 7

            if self.board.has_queenside_castling_rights(chess.WHITE):
                init_piece[7] = 7

            if self.board.has_queenside_castling_rights(chess.BLACK):
                init_piece[56] = 7


            if self.board.ep_square is not None:
                init_piece[self.board.ep_square] = 8
                print("able to use en passant")


        init_piece = np.reshape(init_piece, (8,8))
        print(init_piece)



s = state()
s.initialize()
