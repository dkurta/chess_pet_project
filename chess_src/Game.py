from chess_src.Util import print_board_and_score, choose_move, validate_move

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
            self.bot_color = chess.BLACK
            print("you're white.")
        else:
            self.player_color = chess.BLACK
            self.bot_color = chess.WHITE
            print("you're black.")

    def play(self):
        """
        Function for playing a chess game. Asks player for moves and makes move suggested by Negamax.
        :param game: The starting state of the game.
        :return: 
        """
        while not self.is_finished():
            print_board_and_score(self)
            if self.b.turn == self.player_color:
                # player has to move
                valid_move_inserted = False
                while not valid_move_inserted:
                    # while loop for catching invalid moves.
                    move = input('Please enter your move. Possible moves are: \n{}'.format(self.b.legal_moves))
                    move_val = validate_move(move, self)
                    if move_val:
                        self.b.push_san(move_val)
                        valid_move_inserted = True
            else:
                # bot has to move
                print("AI moves.")
                ai_move_san = choose_move(self.b, self.bot_color)
                print("AI's move is {}".format(ai_move_san))
                self.b.push_san(ai_move_san)

    def is_finished(self):
        return self.b.is_game_over()
