#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
if number < 0:
    number = number * -1
    mod = number % 10
    mod = mod * -1
    number = number * -1
if (mod > 5):
    print(f"Last digit of {number} is {mod} and is greater than 5")
elif (mod < 6 and mod != 0):
    print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
