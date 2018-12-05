import chess

def evaluate(board):
    '''
    Computes the evaluation score for a chess position
    Positive score means that white is better,
    Negative score means that black is better.
    Zero socre means that the position is equal.
    
    :param board: the board including the position.
    :return: the score for the white player.
    '''
    # at first, check if game is over
    # and evaluate position with 1000, -1000 or 0
    if board.is_game_over():
        res = board.result()
        if res == '1-0':
            return 1000
        elif res == '0-1':
            return -1000
        else:
            return 0

    # piece values according to Capablanca and S.Polgar
    piece_values = {chess.PAWN: 1,
                    chess.BISHOP: 3,
                    chess.KNIGHT: 3,
                    chess.ROOK: 5,
                    chess.QUEEN: 9,
                    chess.KING: 0}

    score = 0
    # add up scores according to piece_values
    for x in board.piece_map().values():
        if x.color:
            # white piece, add
            score += piece_values[x.piece_type]
        else:
            # black piece, subtract
            score -= piece_values[x.piece_type]
    return score
