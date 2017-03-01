#!/usr/bin/env python

"""
    Merge Sort Algorithm
    Author: Gianluca Biccari
    Description: sort an input array of integers and return a sorted array
"""

def merge_sort(iarray):
    if iarray is None or len(iarray) < 2:
        return iarray
    else:
        return __merge_sort(iarray, 0, len(iarray)-1)

def __merge_sort(iarray, first, last):
    # Sort the subarray until you reached one element only
    if last == first:
        # you must return an array of one element, not the int value
        return [iarray[first]]
    else:
        # get the middle position of the subarray
        middle = (last - first) / 2 + first
        # call the sort on the left and right subarrays
        a1 = __merge_sort(iarray, first, middle)
        a2 = __merge_sort(iarray, middle + 1, last)
        # merge and sort a1 and a2, which are already sorted
        return __sort(a1, a2)

def __sort(a1, a2):
    # merge two sorted array
    # we know for sure the lenght of the output array
    N = len(a1) + len(a2)
    # prepare the slots
    res = [None] * N
    idx1 = 0
    idx2 = 0
    for i in xrange(0, N):
        if a1[idx1] <= a2[idx2]:
            res[i] = a1[idx1]
            idx1 = idx1 + 1
            # if we reached the end of a1, then all the rest if just a2
            # because the two arrays we know being sorted
            if idx1 == len(a1):
                res[i+1:] = a2[idx2:]
                break
        else:
            res[i] = a2[idx2]
            idx2 = idx2 + 1
            # if we reached the end of a2, then all the rest if just a1
            # because the two arrays we know being sorted
            if idx2 == len(a2):
                res[i+1:] = a1[idx1:]
                break
    return res
