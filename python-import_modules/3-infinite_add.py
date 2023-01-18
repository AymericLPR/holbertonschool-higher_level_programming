#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    n_num = len(sys.argv) - 1
    if n_num == 1:
        for i in range(1, n_num + 1):
            print("{}".format(sys.argv[i]))
    elif n_num > 1:
        for i in range(1, n_num + 1):
            x = x + int(sys.argv[i])
        print("{}".format(x))
    else:
        print("0")
