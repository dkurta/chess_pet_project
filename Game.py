import chess


class Game:
    def __init__(self):
        self.b = chess.Board()
        player_color = input("Pick w/b")
        if player_color == "w":
            self.player_color = chess.WHITE
            print("you're white.")
        else:
            self.player_color = chess.BLACK
            print("you're black.")
        print(self.b.legal_moves)
