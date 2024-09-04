#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if number < 0:
last_digit = -last_digit

if number > 5:
print(f"")
