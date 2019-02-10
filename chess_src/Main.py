from chess_src.Game import Game
from chess_src.Util import play


if __name__ == '__main__':
    # g = Game(fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    # g = Game(fen='rnbqkb1r/pppppppp/7n/8/4P1P1/8/PPPP1P1P/RNBQKBNR b KQkq - 0 1')
    # g = Game(fen="r5k1/pq1nR1pp/1p3r2/5p2/3P4/3B1b1Q/P4PPP/R5K1 w - - 0 1")
    # s = translate('Springer nach d6')
    # print(s)
    # while True:
    #     move = input('Please enter your move:')
    #     s = translate(move)
    #     print(s)
    g = Game()
    g.play()
