#!/usr/bin/env python

"""
    Insertion Sort Algorithm
    Description: sort an input array of integers and return a sorted array
"""

def insertion_sort(iarray):
    if iarray is None or len(iarray) < 2:
        return iarray
    else:
        N = len(iarray)
        # first element of array already in order, at pos 0
        # start scanning the following elements
        for j in range(1, N):
            print("{}|{}".format(iarray[:j], iarray[j]))
            # for each scanned element position it inside the
            # already sorted array going from 0 to J-1
            for i in range(0, j):
                # place element in the right position
                if iarray[j] <= iarray[i]:
                    tmp = iarray[j]
                    iarray[i+1:j+1] = iarray[i:j]
                    iarray[i] = tmp
                    break
        return iarray
