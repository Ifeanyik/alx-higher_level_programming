#!/usr/bin/python3
import sys
length = len(sys.argv)
if __name__ == "__main__":
    i = 1
    sum = 0
    while i < length:
        sum += int(sys.argv[i])
        i += 1
    print("{}".format(sum))
