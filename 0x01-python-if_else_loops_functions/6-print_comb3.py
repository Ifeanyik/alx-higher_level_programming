#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if int(str(i) + str(j)) == 89:
            print("{:02d}".format(int(str(i) + str(j))))
        else:
            print("{:02d}, ".format(int(str(i) + str(j))), end="")
