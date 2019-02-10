"""The class 'Game' is a wrapper of a chess.Board from the python module.
It also holds a method to play the game.
"""

from chess_src.Util import print_board_and_score, validate_move, get_pretty_move_list
from chess_src.Negamax import choose_move

import chess

RESULT_TO_MESSAGE_MAPPING = {'1-0': "White has won the game.",
                             '0-1': "Black has won the game.",
                             '1/2-1/2': "The game ended in a draw."}


class Game:
    def __init__(self, fen=None):
        if fen:
            self.b = chess.Board(fen)
        else:
            self.b = chess.Board()
        #fen = input()
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
                    move = input('\nPlease enter your move. Possible moves are: {}.'.format(get_pretty_move_list(self)))
                    move_val = validate_move(move, self)
                    if move_val:
                        self.b.push_san(move_val)
                        valid_move_inserted = True
            else:
                # bot has to move
                print("\nAI is thinking...")
                ai_move_san = choose_move(self.b, self.bot_color)
                print("AI's move is {}".format(ai_move_san))
                self.b.push_san(ai_move_san)
        # game is finished
        self.print_ending_message()

    def is_finished(self):
        """
        :return: True if game is finished. Otherwise False. 
        """
        return self.b.is_game_over()

    def print_ending_message(self):
        """
        Prints a greeting message according to the result.
        """
        print("The game is over. {} Thank you for playing!".format(RESULT_TO_MESSAGE_MAPPING[self.result()]))

