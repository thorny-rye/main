from math import inf

def divide(first, second):
    if second > 0:
        res = first / second
        return res
    elif second == 0:
        return inf