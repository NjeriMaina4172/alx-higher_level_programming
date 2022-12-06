#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    # a program to do infinite addition

    if (len(argv) < 2):
        print("0")
    elif (len(argv) == 2):
        print(argv[1])
    else:
        dup = [int(argv[i]) for i in range(1, len(argv))]
        Sum = sum(dup)
        print(Sum)
