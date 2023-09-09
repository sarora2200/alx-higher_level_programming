#!/usr/bin/env python3
#5-main_c.py

def no_c(my_string):

    string = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(string))
