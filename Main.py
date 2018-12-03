import chess
from Game import Game
from Negamax import negamax

def play(game):
    ## True = chess.WHITE, False = chess.BLACK
    if game.b.turn == game.player_color:
        move = input('Please enter your move: \n{}'.format(game.b.legal_moves))
        game.b.push_san(move)
    else:
        print("AI moves.")
        ## negamax here
        negamax(game.b)

if __name__ == '__main__':
    g = Game()
    print(g.b)
    # while not g.b.is_game_over():
    play(game=g)
