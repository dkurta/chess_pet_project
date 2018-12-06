from Evaluation import evaluate
from Game import Game
from Negamax import pick_best_move


def play(game):
    while not game.b.is_game_over():
        # Print Board at first
        print('\n')
        print(game.b)
        print('Evaluation Score: {}'.format(evaluate(g.b)))
        ## True == chess.WHITE, False == chess.BLACK
        if game.b.turn == game.player_color:
            move = input('Please enter your move: \n{}'.format(game.b.legal_moves))
            game.b.push_san(move)
        else:
            print("AI moves.")
            ai_move_san = pick_best_move(game.b, not game.player_color, depth=3)
            print("AI's move is {}".format(ai_move_san))
            game.b.push_san(ai_move_san)

        # move = input('Please enter your move: \n{}'.format(game.b.legal_moves))
        # game.b.push_san(move)
        # print('Evaluation Score: {}'.format(evaluate(g.b)))

if __name__ == '__main__':
    g = Game()
    play(game=g)
