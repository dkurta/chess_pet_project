import chess

# piece values according to Capablanca
PIECE_VALUES = {chess.PAWN: 1,
                chess.BISHOP: 3,
                chess.KNIGHT: 3,
                chess.ROOK: 5,
                chess.QUEEN: 9,
                # number of kings is always equal
                chess.KING: 0}

def evaluate(board, color="WHITE"):
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
        # white won the game
        if res == '1-0':
            return 1000
        # black won
        elif res == '0-1':
            return -1000
        # game drawn
        else:
            return 0


    score = 0
    # add up scores according to piece_values
    for piece in board.piece_map().values():
        if piece.color:
            # white piece, add
            score += PIECE_VALUES[piece.piece_type]
        else:
            # black piece, subtract
            score -= PIECE_VALUES[piece.piece_type]
    if color == "WHITE":
        return score
    else:
        return -score
