"""
Author(s): ...
Creation date: 15/02/2025
Last modification: 15/02/2025

Description: A python class introducing a class containing a chessboard and all related information to play a game.
"""

### DESCRIPTION/PLAN SECTION ###
'''
A game is going to work like this:

    - A chessboard is initialised
    - Related class variables are initialised (last move played, possible moves, pieces list...)
    - According to the last move and current chessboard situation, a list of possible moves is created
    - A move is then selected (randomly or not) and makes the chessboard evolve

NOT TO FORGET:
O-O and O-O-O aren't possible if rook/king already moved, or one of squares concerned by the move can check the king
En passant rule
A move mustn't let an ally king checked (for this, when moving a piece linked to a king, must check what is the first piece on the same row/column/diag)
3 exact same positions must lead to a draw
30 (?) moves without any pawn moves and no pieces taken must lead to a draw
'''

from Chessboard import Chessboard

class Game:
    def __init__(self):
        '''
        Constructor defining chessboard and all related variables for the game
        '''
        self.chessboard = Chessboard()

        # Indicates the last move played
        self.last_move = None

        # Indicate the possible moves
        self.possible_moves = []

        # Indicates the number of moves played
        self.nb_moves = 0

        # Indicate if a kings are checked or not
        self.is_white_king_checked = False
        self.is_black_king_checked = False

        # Indicate if rooks/kings moved for eventual O-O or O-O-O
        self.white_king_moved = False
        self.a1_rook_moved = False
        self.h1_rook_moved = False

        self.black_king_moved = False
        self.a8_rook_moved = False
        self.h8_rook_moved = False

        # Indicate the number of moves without pawn moves or pieces taken
        self.passive_moves = 0

        # List of chessboard's states during the game. self.chessboard is appended after each move
        self.chessboard_historic = []

        # List of possible moves at each state of the game. self.possible_moves is appended after each move
        self.possible_moves_historic = []

    def move(self):
        ''' 
        Choose a move in possible moves lists and update the chessboard
        '''

        # ...

        # Update pinned and unpinned pieces

        # Update taken pieces

        # Update checked kings

        # Update last move, chessboard, nb_moves, nb_passive_moves ...

        pass

    def possible_moves(self):
        '''
        Update the list of possible moves (possible_moves) for a given Chessboard's Game
        '''
        # Check if a king is checked or not

        # Identify pieces that are pinned (and that cannot move as a consequence)

        # For other pieces, add all accessible cases, including cases with an opponent piece

        # Check eventual en passant moves

        # Check eventual O-O or O-O-O moves


        pass
