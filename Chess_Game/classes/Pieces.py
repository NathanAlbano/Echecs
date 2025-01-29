"""
Author(s): ...
Creation date: 12/18/2024
Last modification: 12/18/2024

Description: A Python class introducing every piece used in a chessboard game.
"""
from resources.global_variables import NB_SQUARES, NATURE

class Piece:
    def __init__(self, nature, x, y, value, side):
        self.nature = nature  # Type of piece (king, queen, rook, etc.)
        self.x = x  # X-coordinate (column)
        self.y = y  # Y-coordinate (row)
        self.value = value  # Piece value (e.g., 1 for pawn, 9 for queen)
        self.side = side  # "white" or "black"

    def move(self, new_x, new_y):
        """Checks if the move is valid before updating the position."""
        if self.is_valid_move(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True
        return False

    def is_valid_move(self, new_x, new_y):
        """Validates movement based on the piece type."""
        dx, dy = abs(new_x - self.x), abs(new_y - self.y)

        if self.nature == "pawn":
            direction = 1 if self.side == "white" else -1  # White moves up, Black moves down
            return dx == 0 and (new_y - self.y == direction or (self.y == (1 if self.side == "white" else 6) and new_y - self.y == 2 * direction))

        elif self.nature == "rook":
            return dx == 0 or dy == 0  # Moves in a straight line

        elif self.nature == "bishop":
            return dx == dy  # Moves diagonally

        elif self.nature == "queen":
            return dx == dy or dx == 0 or dy == 0  # Moves in a straight line or diagonally

        elif self.nature == "king":
            return dx <= 1 and dy <= 1  # Moves 1 square in any direction

        elif self.nature == "knight":
            return (dx, dy) in [(1, 2), (2, 1)]  # Moves in an L-shape

        return False  # Invalid move if the piece type is unknown

    def __repr__(self):
        return f"{self.nature}({self.x}, {self.y}, {self.side})"

# Example usage
p1 = Piece(NATURE[1], 1, 1, VALUE[3], "white")
print(p1.move(1, 4))  # True (valid move)
print(p1.move(3, 3))  # True (valid move)
print(p1.move(4, 5))  # True (valid move)
print(p1.move(2, 1))  # True (valid move)
