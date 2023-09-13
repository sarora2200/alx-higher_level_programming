#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weighted = sum(score * weight for score, weight in my_list)
    totalWeight = sum(weight for _, weight in my_list)
    return total_weighted / totalWeight
