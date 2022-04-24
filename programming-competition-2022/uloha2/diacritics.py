#!/usr/bin/python


import unicodedata


def remove_diacritics(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass
    text = unicodedata.normalize('NFD', text).encode(
        'ascii', 'ignore').decode("utf-8")
    return str(text)


def has_diacritics(text):
    return text != remove_diacritics(text)
