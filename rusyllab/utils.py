from .rusyllab import split


def split_word(word):
    """
    Split single word to syllables
    :param word: unicode string representing Russian word
    :return: list of unicode strings for syllables
    """
    return split(word)


def split_words(words):
    """
    Split the words in list to contiguous list of sillables and word separators (single space chars)
    :param words: list of words (unicode strings)
    :return: list of tokens - syllables and spaces
    """
    tokens = []
    for word in words:
        sx = split(word)
        if len(tokens) > 0:
            tokens.append(u' ')
        tokens.extend(sx)
    return tokens
