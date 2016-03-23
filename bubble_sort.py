"""
    Bubble Sort Algorithm
    Author: Gianluca Biccari
    Description: sort an input array of integers and return a sorted array
"""

def bubble_sort(iarray):
    switched = True
    n = len(iarray)
    while switched:
        switched = False
        for i in xrange(0, n-1):
            if iarray[i] > iarray[i+1]:
                iarray[i], iarray[i+1] = iarray[i+1], iarray[i]
                switched = True
    return iarray
