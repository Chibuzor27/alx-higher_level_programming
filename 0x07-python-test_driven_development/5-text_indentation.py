#!/usr/bin/python3
"""Indent module"""


def text_indentation(text):
    """Indent text"""

    if text is None or type(text) != str:
        raise TypeError('text must be a string')

    if len(text) == 0:
        return

    line = 0
    space = -1
    for i in range(0, len(text)):
        if line == 1 and space == 0:
            print(f'\n\n', end="")
            line = 0
            space = -1
            if text[i] != ' ':
                print(text[i], end="")
                space = 0
            continue

        if space == -1 and text[i] == ' ':
            continue

        if space == 0 and text[i] == ' ':
            space = 1
            continue

        if space == 1 and text[i] == ' ':
            continue

        if space == 1 and text[i] != ' ' \
                and text[i] != '.' and text[i] != '?' and text[i] != ':':
            print(' ', end="")

        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end="")
            line = 1
            space = 0
            if (i == len(text) - 1):
                print(f'\n\n', end="")
            continue

        print(text[i], end="")
        space = 0
