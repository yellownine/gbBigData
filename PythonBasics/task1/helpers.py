import sys


def getUserNumber(msg):
    try:
        userNum = int(input(msg))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        sys.exit(1)
    return userNum
