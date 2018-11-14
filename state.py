import chess
import numpy as np


class State():
    def __init__(self, board=None):
        if board is not None:
            self.board = board
        else:
            self.board = chess.Board()

    def list(self):
        return self.board.pseudo_legal_moves

    def clean(self):
        return self.board.clear()

    def serialize(self):
        # binary state
        state = np.zeros((5,8,8))
        init_piece = np.zeros(64, int)

        for idx in range(64):
            symbol = self.board.piece_at(idx)

            if symbol is not None:
                init_piece[idx] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                 "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[symbol.symbol()]


            if self.board.has_kingside_castling_rights(chess.WHITE):
                init_piece[0] = 7

            if self.board.has_kingside_castling_rights(chess.BLACK):
                init_piece[63] = 7+8

            if self.board.has_queenside_castling_rights(chess.WHITE):
                init_piece[7] = 7

            if self.board.has_queenside_castling_rights(chess.BLACK):
                init_piece[56] = 7+8


            if self.board.ep_square is not None:
                init_piece[self.board.ep_square] = 8
                # print("able to use en passant")


        init_piece = init_piece.reshape(8,8)
        # print(init_piece)

        # 0-3 columns to binary
        state[0] = (init_piece>>3)&1
        state[1] = (init_piece>>2)&1
        state[2] = (init_piece>>1)&1
        state[3] = (init_piece>>0)&1

        # 4th column is who's turn it is
        state[4] = (self.board.turn*1.0)
        # print(state)

        # 257 bits according to readme
        return state

        # return init_piece



if __name__ == "__main__":
    s = State()
    s.serialize()
