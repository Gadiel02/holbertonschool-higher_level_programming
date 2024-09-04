#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if number < 0:
    last_digit = -last_digit

print("The last digit of", number,)

if last_digit>5:
    print("is greater than 5")

elif last_digit == 0:
    print("is 0")

elif 6 > last_digit and last_digit != 0:
    print("is less than 6 and not 0")
    