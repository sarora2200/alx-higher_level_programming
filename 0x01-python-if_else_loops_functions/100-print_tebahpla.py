#!/usr/bin/python3
i = 0
for c in range(122, 96, -1):
    print("{:c}".format(c - i), end="")
    i = 32 if i == 0 else 0
