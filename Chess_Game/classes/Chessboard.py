"""
Author(s): ...
Creation date: 12/18/2024
Last modification: 12/18/2024

Description: A python class introducing a chessboard's mathematical representation 
"""
import numpy as np
from .Pieces import Piece
from ..resources.global_variables import NB_SQUARES, NATURE

class Chessboard:
    '''
    No parameters to build the chessboard.
    The chessboard is represented by an pieces array. You can find the different pieces' numero in ./Pieces.py
    '''
    def __init__(self):
        '''
        Builds a 8*8 chessboard with 0 (no pieces)
        '''
        # self.int_chessboard = np.zeros((8,8))
        self.chessboard = np.full(fill_value=Piece(nature="square", x=any, y=any, side=any), shape=(8,8))

        column_to_letter = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
        self.index_to_square = {}
        for i in range(NB_SQUARES):
            for j in range(NB_SQUARES):
                self.index_to_square[(i,j)] = f"{column_to_letter[i]}{j+1}"

        self.init_chessboard()

    def init_chessboard(self):
        for column in range(NB_SQUARES):
            self.chessboard[1,column] = Piece(nature="pawn", x=1, y=column, side="white")
            self.chessboard[6,column] = Piece(nature="pawn", x=6, y=column, side="black")

            for row in range(2,6):
                self.chessboard[row,column] = Piece(nature="square", x=row, y=column, side="neutral")

            if column == 0 or column == 7:
                self.chessboard[0,column] = Piece(nature="rook", x=0, y=column, side="white")
                self.chessboard[7,column] = Piece(nature="rook", x=7, y=column, side="black")

            elif column == 1 or column == 6:
                self.chessboard[0,column] = Piece(nature="knight", x=0, y=column, side="white")
                self.chessboard[7,column] = Piece(nature="knight", x=7, y=column, side="black")

            elif column == 2 or column == 5:
                self.chessboard[0,column] = Piece(nature="bishop", x=0, y=column, side="white")
                self.chessboard[7,column] = Piece(nature="bishop", x=7, y=column, side="black")

            elif column == 3:
                self.chessboard[0,column] = Piece(nature="queen", x=0, y=column, side="white")
                self.chessboard[7,column] = Piece(nature="king", x=7, y=column, side="black")

            else:
                self.chessboard[0,column] = Piece(nature="king", x=0, y=column, side="white")
                self.chessboard[7,column] = Piece(nature="queen", x=7, y=column, side="black")

    def print_chessboard(self):
        print(self.chessboard)

'''
## === TEST SECTION === ##
test = Chessboard()
print(test.index_to_square[(7,7)])
print(test.chessboard)
'''
