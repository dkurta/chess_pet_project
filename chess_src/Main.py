from Evaluation import evaluate
from Game import Game
from MoveDSL import translate

from chess_src.Negamax import assign_scores


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
            ai_move_san = assign_scores(game.b, game.bot_color, depth=3)
            print("AI's move is {}".format(ai_move_san))
            game.b.push_san(ai_move_san)

        # move = input('Please enter your move: \n{}'.format(game.b.legal_moves))
        # game.b.push_san(move)
        # print('Evaluation Score: {}'.format(evaluate(g.b)))

if __name__ == '__main__':
    # g = Game(fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    # g = Game(fen='rnbqkb1r/pppppppp/7n/8/4P1P1/8/PPPP1P1P/RNBQKBNR b KQkq - 0 1')
    # g = Game(fen="r5k1/pq1nR1pp/1p3r2/5p2/3P4/3B1b1Q/P4PPP/R5K1 w - - 0 1")
    s = translate('Springer nach d6')
    print(s)
    while True:
        move = input('Please enter your move:')
        s = translate(move)
        print(s)
    # g = Game()
    # play(game=g)
