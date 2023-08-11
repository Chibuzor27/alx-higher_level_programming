#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    size = len(argv)

    if size <= 1:
        print('{} arguments.'.format(0))
    else:
        print('{} argument{:s}:'.format(size - 1, "s" if size > 2 else ""))
        for i in range(1, size):
            print('{}: {}'.format(i, argv[i]))
