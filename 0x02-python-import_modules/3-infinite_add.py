#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    arg_sum = 0
    for i, arg in enumerate(argv[1:]):
        arg_sum += int(arg)

    print('{:d}'.format(arg_sum))