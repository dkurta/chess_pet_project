from chess_src.Evaluation import evaluate
from chess_src.Negamax import choose_move
from chess_src.MoveDSL import translate


def print_board_and_score(game):
    """
    Prints the board and it's score. 
    :param game: actual game, instance of src_chess.Game 
    :return: 
    """
    print('\n')
    print(game.b)
    print('Evaluation Score: {}'.format(evaluate(game.b)))


def validate_move(move, game):
    """
    Checks if the move entered by the player is in a list of moves. Also tries to translate them from German Chess DSL. 
    :param move: move as String. e.g. "dxe6" or "Bauer d schlägt e6" 
    :param game: the game state. needed for the list of regular moves.
    :return: the move if move is in the list. False if not.
    """
    move_list_uci = list(game.b.legal_moves)
    # convert to san format
    move_list_san = list(map(lambda m: game.b.san(m), move_list_uci))
    if move in move_list_san:
        return move
    try:
        translated_move = translate(move)
    except KeyError:
        # Key Error gets raised if move is not translatable
        return False
    if translated_move in move_list_san:
        return translated_move
    return False


def execute_move(move, game):
    """
    Execute move
    :param move: move in san format 
    :param game: game state
    :return: 
    """
    game.b.push_san(move)
