#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print(f'{number}', end="")
        return 0
    elif number > 0:
        print(f'{number % 10}', end="")
        return number % 10
    else:
        print(f'{abs(number % -10)}', end="")
        return abs(number % -10)