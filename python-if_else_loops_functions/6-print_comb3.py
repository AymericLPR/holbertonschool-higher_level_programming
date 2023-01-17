#!/usr/bin/python3
for i in range(0, 8):
    for x in range(0, 10):
        if i < x:
            print("{:1d}{:1d}".format(i, x), end=", ")
print("89")
