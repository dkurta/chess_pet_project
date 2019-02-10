""" This file contains methods to translate the German Chess DSL 
    to tha standard san chess notation.
    The code is programmed as functional as possible beeing stateless and using lambda expressions
    and only constants, using a closure to hide a counter from outer scope and having all functions
    without side effects.
    

SYNTAX of the German Chess DSL:

    {figureType (required)} {action (required)} {file or rank (not required)} \
    {field (required)} {figureTypeConversion (note required)} {Schach/Schachmatt (not required)}"   
    or
    "{kurze Rochade | lange Rochade (required)} {Schach/Schachmatt (not required)}" 


Examples for the German Chess DSL:

    "Bauer nach d6" -> "d6"
    "Bauer c schlägt d6" -> "cxd6"
    "Turm f nach e1" -> "Rfe1"
    "Springer schlägt f3 Schach" -> "Nxf3+"
    "Bauer b schläg a8 Dame" -> "bxa8=Q"
    "kurze Rochade" -> "0-0"
    "Läufer schlägt e5 Schachmatt" -> "Bxe5++"
"""


TRANSLATION_PIECES = {'Springer':  'N',
                       'Turm':      'R',
                       'Bauer':     '',
                       'Läufer':    'B',
                       'Dame':      'Q',
                       'König':     'K'}

TRANSLATIONS_ACTION = {'schlägt':   'x',
                       'nach':       ''}

TRANSLATION_SPECIAL = {'kurze Rochade': '0-0',
                       'lange Rochade': '0-0-0'}

TRANSLATION_CHECKS =  {'Schach': '+',
                       'Schachmatt': '++'}

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# shift letters from FILES by 48 to recieve ROWS
# ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
RANKS = list(map(lambda s: str(chr(ord(s)-48)), FILES))


def translate(dsl_string):
    """
    Translates a String in a German Domain Specific Language to the common Chess Notation DSL.
    :param dsl_string: the german dsl input String 
    :return: move as standard Chess Notation
    """
    if dsl_string in TRANSLATION_SPECIAL.keys():
        return TRANSLATION_SPECIAL[dsl_string]

    token = dsl_string.strip().split(" ")

    # check if last word is "Schach" or "Schachmatt" and append symbol at the end of the method
    last_symbol = []
    if token[-1] in TRANSLATION_CHECKS.keys():
        last_symbol.append(TRANSLATION_CHECKS[token[-1]])
        del token[-1]

    # Handle case of casteling
    if ' '.join(token[0:2]) in TRANSLATION_SPECIAL.keys():
        result = TRANSLATION_SPECIAL[' '.join(token[0:2])]
        if last_symbol:
            result += last_symbol[0]
        return result

    counter = closure_for_counter()
    translated_token = list()
    # e.g. "Springer"
    translated_token.append(TRANSLATION_PIECES[token[counter()]])

    if token[counter(inc=False)+1] in FILES or token[counter(inc=False)+1] in RANKS:
        # e.g. "a"/"1"
        translated_token.append(token[counter()])

    # e.g. "nach"
    translated_token.append(TRANSLATIONS_ACTION[token[counter()]])
    # e.g. "f3"
    translated_token.append(token[counter()])
    if counter() == len(token) - 1:
        # e.g. "Dame"
        translated_token.append('={}'.format(TRANSLATION_PIECES[token[counter(inc=False)]]))
    return ''.join(translated_token + last_symbol)


def closure_for_counter():
    """
    a closure function for the generation of a counter that starts with 0
    :return: a counter() function with a counter variable that can not be accessed or manipulated from outside.
    """
    x = -1

    def increment(inc=True):
        """
        :param inc: if True: increment and return counter. if False: return counter without incrementation.
        :return: int value from of the counter variable. 
        """
        nonlocal x
        if inc:
            x += 1
        return x
    return increment
