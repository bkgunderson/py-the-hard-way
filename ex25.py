def break_words(stuff):
    """
    This function will break up words for us.
    :param stuff:
    :return words:
    """
    words = stuff.split(' ')
    return words


def sort_words(words):
    """
    Sorts the words.
    :param words:
    :return sorted(words):
    """
    return sorted(words)


def print_first_word(words):
    """
    Prints the first word after popping it off.
    :param words:
    :return word:
    """
    word = words.pop(0)
    print word


def print_last_word(words):
    """
    Prints the last word after popping it off.
    :param words:
    :return word:
    """
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """
    Takes in a full sentence and returns the sorted words.
    :param sentence:
    :return sort_words(words):
    """
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """
    Prints the first and last words of the sentence.
    :param sentence:
    :return print_first_word(words):
    :return print_last_word(words):
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """
    Sorts the words then prints the first and last one.
    :param sentence:
    :return print_first_word(words):
    :return print_last_word(words):
    """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
