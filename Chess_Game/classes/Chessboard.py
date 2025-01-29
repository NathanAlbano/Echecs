"""
Author(s): ...
Creation date: 12/18/2024
Last modification: 12/18/2024

Description: A python class introducing a chessboard's mathematical representation 
"""
import numpy as np
from ..resources.global_variables import NB_SQUARES, NATURE

class Chessboard:
    '''
    No parameters to build the chessboard.
    The chessboard is represented by an integer array. Each piece has a different numero, 0 meaning that no pieces is 
    on a square. You can find the different pieces' numero in ./Pieces.py
    '''
    def __init__(self):
        '''
        Builds a 8*8 chessboard with 0 (no pieces)
        '''
        self.chessboard = np.zeros((8,8))

        column_to_letter = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
        self.index_to_square = {}
        for i in range(NB_SQUARES):
            for j in range(NB_SQUARES):
                self.index_to_square[(i,j)] = f"{column_to_letter[i]}{j+1}"

    def print_chessboard(self):
        print(self.chessboard)

## === TEST SECTION === ##
test = Chessboard()
print(test.index_to_square[(7,7)])
print(test.chessboard)
