import chess

def evaluate(board):
    '''
    Computes the evaluation score for a chess position
    :param board: the board including the position
    :return: the score for the white player 
    '''
    # at first, check if game is over
    if board.is_game_over():
        res = board.result()
        if res == '1-0':
            return 1000
        if res == '0-1':
            return -1000
        if res == '1/2-1/2':
            return 0

    # piece values according to Capablanca and S.Polgar
    piece_values = {chess.PAWN: 1,
                    chess.BISHOP: 3,
                    chess.KNIGHT: 3,
                    chess.ROOK: 5,
                    chess.QUEEN: 9,
                    chess.KING: 0}

    score = 0
    for x in board.piece_map().values():
        if x.color:
            score += piece_values[x.piece_type]
        else:
            score -= piece_values[x.piece_type]
    return score
