#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    num_args = len(sys.argv)
    if num_args == 1:
        print("Number of argument: 0.")
    elif num_args == 2:
        print("Number of argument: 1:")
    else:
        print("Number of arguments:", num_args)

if num_args > 1:
    print()
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
