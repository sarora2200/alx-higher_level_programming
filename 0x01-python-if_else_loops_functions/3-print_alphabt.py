#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 113 or letter == 120:
        continue
    print(chr(letter), end="")
