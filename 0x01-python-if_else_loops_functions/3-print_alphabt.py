#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 113:
         continue
    if letter == 120:
        continue
    print("{:c}".format(letter), end="")

