"""Implementation of the Negamax algorithm. See https://en.wikipedia.org/wiki/Negamax."""

from chess_src.Evaluation import evaluate

CALCULATION_DEPTH = 3


def choose_move(board, color, depth=CALCULATION_DEPTH):
    """
    compute the move with the best scores from Negamax.
    :param board: actual board state
    :param color: color of the player to move
    :param depth: calculation depth
    :return: the best move
    """
    moves_with_score = {}
    for move in board.legal_moves:
        # make copy of the board an call negamax and store values in dict
        successor_board = board.copy()
        successor_board.push(move)
        moves_with_score[board.san(move)] = -negamax(successor_board, not color, depth-1)
        print(board.san(move) + "::::" + str(moves_with_score[board.san(move)]) + "<---------!!!!!!!!""\n")
    # pick the best move
    top_move = ('', float("-infinity"))
    for san, score in moves_with_score.items():
        if score > top_move[1]:
            top_move = (san, score)
    print(top_move)
    return top_move[0]


def negamax(board, color, depth):
    """
    implementation of the Negamax algorithm
    :param board: the board (position)
    :param color: color of the player to move.
    :param depth: depth for the searching tree
    :return: the score for the player regarding the evaluation scores from the search tree
    """
    if depth == 0:
        if color:
            return evaluate(board, "WHITE")
        else:
            return evaluate(board, "BLACK")
    value = float("-infinity")
    for move in board.legal_moves:
        board_child = board.copy()
        board_child.push(move)
        value = max(value, -negamax(board_child, not color, depth-1))
    return value
