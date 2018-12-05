import chess


class Game:
    def __init__(self, fen=None):
        if fen:
            self.b = chess.Board(fen)
        else:
            self.b = chess.Board()
        player_color = input("Pick w/b")
        if player_color == "w":
            self.player_color = chess.WHITE
            print("you're white.")
        else:
            self.player_color = chess.BLACK
            print("you're black.")
