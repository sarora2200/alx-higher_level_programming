#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'r') as f:
        for i in f:
            print(i, end="")
    f.close()
