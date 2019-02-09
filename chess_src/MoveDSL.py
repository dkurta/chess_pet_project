TRANSLATION_PIECES = {'Springer':  'N',
                       'Turm':      'R',
                       'Bauer':     '',
                       'Läufer':    'B',
                       'Dame':      'Q',
                       'König':     'K'}

TRANSLATIONS_ACTION = {'schlägt':   'x',
                       'nach':       ''}

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# shift letters from FILES by 48 to recieve ROWS
# ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
ROWS = list(map(lambda s: str(chr(ord(s)-48)), FILES))


def translate(dsl_string):
    """
    Translates a String in a German Domain Specific Language to the common Chess Notation DSL.
    :param dsl_string: the german dsl input String 
    :return: move as standart Chess Notation
    """
    token = dsl_string.strip().split(" ")
    counter = closure_for_counter()
    translated_token = list()
    # e.g. "Springer"
    translated_token.append(TRANSLATION_PIECES[token[counter()]])

    if token[counter(inc=False)+1] in FILES or token[counter(inc=False)+1] in ROWS:
        # e.g. "a"/"1"
        translated_token.append(token[counter()])

    # e.g. "nach"
    translated_token.append(TRANSLATIONS_ACTION[token[counter()]])
    # e.g. "f3"
    translated_token.append(token[counter()])
    if counter() == len(token) - 1:
        # e.g. "Dame"
        translated_token.append('={}'.format(TRANSLATION_PIECES[token[counter(inc=False)]]))
    return ''.join(translated_token)


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
