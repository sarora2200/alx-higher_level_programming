#!/usr/bin/python3
"""module mylist
Creates class that inherits from list class
"""

class MyList(list):
    """class Mylist that inherit from list"""

    def print_sorted(self):
        """prints the list in ascending sort"""

        my_list = self[:]
        my_list.sort()
        print("{}".format(my_list))
