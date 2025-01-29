"""
Author(s): ...
Creation date: 12/18/2024
Last modification: 12/18/2024

Description: A python script to run the chess game with user interface
"""
import subprocess

# file = "classes.Chessboard"
file = "classes.Pieces"

# Using system() method to
# execute shell commands
subprocess.Popen(f'python -m Chess_Game.{file}', shell=True)