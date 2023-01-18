#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_num = len(sys.argv) - 1
    if n_num == 1:
        for i in range(1, n_num + 1):
            print("{}".format(i))
    elif n_arg > 1:
        for i in range(1, n_arg + 1):
            i = i + i
            print("{}".format(i))
    else:
        print("0")
