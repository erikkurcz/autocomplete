import string
import re


def get_words_from_file(filepath):

    with open(filepath, 'r') as data:
        lines = data.read()

    return re.findall('\w+', lines)


def get_words_only(words):
    return re.findall('\w+', words)


def alphabet():
    all_letters = [None]*(2*len(string.ascii_lowercase))
    all_letters[1::2] = string.ascii_lowercase
    all_letters[::2] = string.ascii_uppercase
    return all_letters
