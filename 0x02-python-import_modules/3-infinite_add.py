#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    count = len(argv) - 1
    sum = 0
    for i in range(count):
        sum += int(argv[i + 1])
    print(sum)
