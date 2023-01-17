#!/usr/bin/python3
def uppercase(str):
    final = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            final += chr(ord(i) - 32)
        else:
            final += i
    print("{}".format(final))
