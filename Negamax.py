from Evaluation import evaluate


def assign_scores(board, color, depth):
    '''
    Assign scores to possible moves with negamax. 
    :param board: 
    :param color: 
    :param depth: 
    :return: The move with the best score.
    '''
    moves_with_score = {}
    for move in board.legal_moves:
        successor_board = board.copy()
        successor_board.push(move)
        moves_with_score[board.san(move)] = negamax(successor_board, color, depth)
    return moves_with_score


def negamax(board, color, depth):
    '''
    Implementation of the negamax algorithm
    '''
    if color:
        ## White
        multiplier = 1
    else:
        ## Black
        multiplier = -1

    if depth == 0:
        return multiplier * evaluate(board)

    ## Assign negative infinity as starting value
    value = float("-infinity")

    for move in board.legal_moves:
        successor_board = board.copy()
        successor_board.push(move)
        value = max(value, -negamax(successor_board, not color, depth-1))

    return value

def pick_best_move(board, color, depth):
    '''
    Calls assign scores and picks best move from dict
    :param board: 
    :param color: 
    :param depth: 
    :return: 
    '''
    print('Thinking...')
    moves_with_scores = assign_scores(board, color, depth-1)
    print(moves_with_scores)
    top_move = ('', float("-infinity"))
    for san, score in moves_with_scores.items():
        if score > top_move[1]:
            top_move = (san, score)
    return top_move[0]
