import random

class RandomPlayer():
    def __init__(self, player) -> None:
        self
    def get_move(self, board):
        move = random.choice(list(board.legal_moves))
        return move