#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit  = number % 10 if number > 10 else number % -10
if Last_digit > 5:
    print("Last digit of {} is {} and is greater than 5". format(number, Last_digit))
elif Last_digit == 0:
    print("Last digit of {} is {} and is 0". format(number, Last_digit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0". format(number, Last_digit))
