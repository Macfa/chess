import chess
import numpy as np

class State(object):
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board
    
    def serialize(self):
        assert self.board.is_valid()
        
        zero = np.zeros(64, np.uint8)
        for i in range(64):
            pp = self.board.piece_at(i)
            if pp is not None:
                zero[i] = {"P":1, "N":2, "B":3, "R":4, "Q":5, "K":6, \
                           "p":9, "n":10, "b":11, "r":12, "q":13, "k":14}[pp.symbol()]
        if self.board.has_queenside_castling_rights(chess.WHITE):
            assert zero[0] == 4
            zero[0] = 7
        if self.board.has_kingside_castling_rights(chess.WHITE):
            assert zero[7] == 4
            zero[7] = 7
        if self.board.has_queenside_castling_rights(chess.BLACK):
            assert zero[56] == 4+8
            zero[56] = 7+8
        if self.board.has_kingside_castling_rights(chess.BLACK):
            assert zero[63] == 4+8
            zero[63] = 7+8
                
        if self.board.ep_square is not None:
            assert zero[self.board.ep_square] == 0
            print("excute a ep_square")
#                     zero[self.board.ep_square] = 8
        zero = zero.reshape(8,8)

        # binary state
        state = np.zeros((5,8,8),np.uint8)

        # 0-3 columns to binary
        state[0] = (zero>>3)&1
        state[1] = (zero>>2)&1
        state[2] = (zero>>1)&1
        state[3] = (zero>>0)&1
        
        # 4 column is who's turn it is
        state[4] = (self.board.turn*1)
#         state[4] = (self.board.turn*1.0)
        
        # 257 bits according to readme
#         return state

    def edge(self):
        return list(self.board.legal_moves)
    

if __name__ == "__main__":
    s = State()
#     s.serialize()
#     s.edge()