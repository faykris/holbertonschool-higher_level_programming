#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
        digit = ((-number % 10) * -1)
else:
        digit = (number % 10)
if digit > 5:
        print("Last digit of {:d} is {:d}".format(number, digit), end=" ")
        print("and is greater than 5")
elif digit == 0:
        print("Last digit of {:d} is {:d}".format(number, digit), "and is 0")
else:
        print("Last digit of {:d} is {:d}".format(number, digit), end=" ")
        print("and is less than 6 and not 0")
