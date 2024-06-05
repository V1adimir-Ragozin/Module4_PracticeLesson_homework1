from math import inf
def divide(first, second):
    try:
        return first/second
    except ZeroDivisionError:
        if first == 0:
            raise ValueError('0/0 is undefined')
        if first > 0:
            return float('inf')
        else:
            return float('-inf')



