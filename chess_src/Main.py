"""Entrypoint for the Chess Pet Project. Instanciates a Game (starting from a fen position is also possible)
and calls the play() method."""

from chess_src.Game import Game

if __name__ == '__main__':
    # g = Game(fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1') # example for a specific position in fen format
    g = Game()
    g.play()
