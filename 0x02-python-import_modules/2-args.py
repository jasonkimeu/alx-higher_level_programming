#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    if count >= 1:
        for i in range(count):
            print("{}: {}".format(i + 1, argv[i + 1]))
