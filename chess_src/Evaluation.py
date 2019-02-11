"""This File contains the evaluation function, a core element of the Chess Pet Project.
In the evaluation, a chess position gets mapped to a numeric value. Negative values are better
for the black party, positive values say that white's position is. There are to factors for the evaluation:

a) the material:
    Every type of pieces gets mapped to a numeric value. The value of a pawn is mapped to 1.0
    These values are added up in a positive way for white pieces and negative for black's.

b) the influence on the board:
    The party with more active piecces is often better in chess. That's why every field attacked by a piece 
    of a party gains +0.02 for the score.
"""
import chess

# piece values according to Capablanca
PIECE_VALUES = {chess.PAWN:     1,
                chess.BISHOP:   3,
                chess.KNIGHT:   3,
                chess.ROOK:     5,
                chess.QUEEN:    9,
                # number of kings is always equal
                chess.KING:     0}

RATING_FOR_GAME_WON_BY_WHITE = 1000
RATING_FOR_DRAWN_GAME = 0

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
            return RATING_FOR_GAME_WON_BY_WHITE
        # black won
        elif res == '0-1':
            return -RATING_FOR_GAME_WON_BY_WHITE
        # game drawn
        else:
            return RATING_FOR_DRAWN_GAME

    piece_map = board.piece_map()
    # revert piece map to access field indices of pieces
    inverted_piece_map = {v: k for k, v in piece_map.items()}

    score = 0
    # add up scores according to piece_values
    for piece in piece_map.values():
        if piece.color:
            ## white piece, add
            # add the value of the piece
            score += PIECE_VALUES[piece.piece_type]
            # reward piece with high influence
            score += get_number_of_attacked_fields(piece, inverted_piece_map, board)*0.02
        else:
            ## black piece, subtract
            # add the value of the piece
            score -= PIECE_VALUES[piece.piece_type]
            # reward piece with high influence
            score -= get_number_of_attacked_fields(piece, inverted_piece_map, board)*0.02
    score = round(score, 2)
    if color == "WHITE":
        return score
    else:
        return -score


def get_number_of_attacked_fields(piece, inverted_piece_map, board):
    """
    computes the number of squares attacked by a piece
    :param piece: the piece
    :param inverted_piece_map: a dict that has pieces as key and it's square indice as value
    :return: number of attacked squares
    """
    return len(board.attacks(inverted_piece_map[piece]))
