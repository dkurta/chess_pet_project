from chess_src.Evaluation import evaluate


def assign_scores(board, color, depth):
    '''
    Assign scores to possible moves with negamax.
    :param board:
    :param color:
    :param depth:
    :return: The move with the best score.
    '''
    moves_with_score = {}
    # make copy of the board an call negamax and store values in dict
    for move in board.legal_moves:
        successor_board = board.copy()
        successor_board.push(move)
        moves_with_score[board.san(move)] = -negamax(successor_board, not color, depth-1)
        print(board.san(move) + "::::" + str(moves_with_score[board.san(move)]) + "<---------------------------------------!!!!!!!!!!!!!!!!""\n")
    # pick the best move
    top_move = ('', float("-infinity"))
    for san, score in moves_with_score.items():
        if score > top_move[1]:
            top_move = (san, score)
    print(top_move)
    return top_move[0]


def negamax(board, color, depth):
    if depth == 0:
        return evaluate(board, color)
    value = float("-infinity")
    for move in board.legal_moves:
        board_child = board.copy()
        board_child.push(move)
        value = max(value, -negamax(board_child, not color, depth-1))
    return value
