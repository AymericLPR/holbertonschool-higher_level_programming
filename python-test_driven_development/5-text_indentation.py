#!/usr/bin/python3
""" Doc """


def text_indentation(text):
    """ Doc """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    try:
        while text[i]:
            print(text[i], end="")
            i += 1
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[i], end="\n\n")
                i += 1
                while text[i] == " ":
                    i += 1
    except:
        pass
