#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
exe = 0
if num < 0:
    num *= -1
    exe = 1
last = num % 10
if exe == 1:
    num *= -1
    last *= -1
print("Last digit of {:d} is ".format(num), end="")
if last > 5:
    print("{:d} and is greater than 5".format(last))
elif last == 0:
    print("{:d} and is 0".format(last))
else:
    print("{:d} and is less than 6 and not 0".format(last))