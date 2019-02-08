translations_pieces = {'Springer':  'N',
                       'Turm':      'R',
                       'Bauer':     '',
                       'Läufer':    'B',
                       'Dame':      'Q',
                       'König':     'K'}

translations_action = {'schlägt':   'x',
                       'nach':       ''}

lines = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def translate(dsl_string):
    """
    Translates a String in a German Domain Specific Language to the common Chess Notation DSL.
    :param dsl_string: the german dsl input String 
    :return: move as standart Chess Notation
    """
    print('b' in lines)
    token = dsl_string.split(" ")
    counter = closure_for_counter()
    translated_token = list()
    # e.g. "Springer"
    translated_token.append(translations_pieces[token[counter()]])

    if token[counter(inc=False)+1] in lines:
        # e.g. "a"
        translated_token.append(token[counter()])

    # e.g. "nach"
    translated_token.append(translations_action[token[counter()]])
    # e.g. "f3"
    translated_token.append(token[counter()])
    if counter() == len(token) - 1:
        # e.g. "Dame"
        translated_token.append('={}'.format(translations_pieces[token[counter(inc=False)]]))
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
