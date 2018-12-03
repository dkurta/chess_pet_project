import chess


class Game:
    def __init__(self):
        self.b = chess.Board()
        print(self.b.legal_moves)
