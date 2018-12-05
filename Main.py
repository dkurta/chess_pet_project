import chess

from Evaluation import evaluate
from Game import Game
from Negamax import negamax


def play(game):
    while not g.b.is_game_over():
        # Print Board at first
        print(g.b)
        print('Evaluation Score: {}'.format(evaluate(g.b)))
        ## True == chess.WHITE, False == chess.BLACK
        if game.b.turn == game.player_color:
            move = input('Please enter your move: \n{}'.format(game.b.legal_moves))
            game.b.push_san(move)
        else:
            print("AI moves.")
            ## call negamax here
            negamax(game.b)

        # move = input('Please enter your move: \n{}'.format(game.b.legal_moves))
        # game.b.push_san(move)
        # print('Evaluation Score: {}'.format(evaluate(g.b)))

if __name__ == '__main__':
    g = Game()
    play(game=g)
