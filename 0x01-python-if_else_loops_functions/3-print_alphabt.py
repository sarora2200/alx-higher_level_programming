#!/usr/bin/python3
for letter in range(97, 123):
    if letter != 113 and letter != 120:
        print("{:c}".format(letter), end="")
