"""
    THIS IS NOT FOR BEGINNER, PLEASE IGNORE THIS TASK IF YOU ARE
    NEW TO PROGRAMMING.

    Write a recursive function moving_cummulative_sum() that calculate the
    moving cummulative sum of integer values in a list and returns the
    new list. For example, given a list [5,6,7,1,2,3], the resulting list
    is [5,11,18,19,21,24].

    This is an open-ended question in which you are free to determine
    the number of parameters for the function, with the first argument is
    for the list such as moving_cummulative_sum(x) with x being the
    list to be operated on.
"""

def moving_cumulative_sum(x : list, i=0):
    if (i >= len(x)): return x
    else:
        if (i == 0): return moving_cumulative_sum(x, i + 1)
        else:
            x[i] = x[i] + x[i - 1]
            return moving_cumulative_sum(x, i + 1)

print(moving_cumulative_sum([5,6,7,1,2,3]))