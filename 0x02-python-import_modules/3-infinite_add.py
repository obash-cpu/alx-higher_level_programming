#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    newsum = 0
    if len(argv) > 1:
        for i in range(1, len(argv)):
            newsum += int(argv[i])

    print(newsum)
