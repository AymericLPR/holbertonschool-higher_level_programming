#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    word = dir(hidden_4)
    for i in range(len(word)):
        if word[i][0] == "_":
            continue
        print("{}".format(word[i]))
