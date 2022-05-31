#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
new_num = str(number)
last = new_num[len(new_num) - 1]
print(f"Last digit of {number} is {last}", end=" ")
if int(last) > 5:
    print("and is greater than 5")
elif int(last) == 0:
    print("and is 0")
elif int(last) < 6 and int(last) != 0:
    print("and is less than 6 and not 0")

