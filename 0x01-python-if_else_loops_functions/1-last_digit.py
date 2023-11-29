#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_Digit = abs(number) % 10 if number > 0 else int(repr(number)[-1]) * -1

print("Last digit of {} is {} ".format(number, lastDigit), end="")

if last_Digit > 5:
            print("and is greater than 5")
elif last_Digit == 0:
            print("and is 0")
else:
            print("and is less than 6 and not 0")
