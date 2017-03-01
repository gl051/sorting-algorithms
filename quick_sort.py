#!/usr/bin/env python

""""
    Quick Sort Algorithm
    Author: Gianluca Biccari
    Description: sort an input array of integers and return a sorted array
"""

def quick_sort(iarray):
    if (iarray is None) or len(iarray) == 0:
        return iarray
    else:
        # divide and conquer alghorithm -> recursive implementation
        __quicksort(iarray, 0, len(iarray)-1)
        return iarray

# in palce sorting on a subarray delimited by first and last
def __quicksort(array, first, last):
    # we stop when first and last do not delimit a subarray anymore.
    if last <= first:
        return
    else:
        # all the sorting is done in the parition on the pivot value
        pvt_idx = partition(array, first, last)
        # the pivot is in the right pos now,  x x x x PVT y y y y
        # where x <= PVT < y. Recursive call on the subarray.
        __quicksort(array, first, pvt_idx - 1)
        __quicksort(array, pvt_idx + 1, last)

def partition(array, first, last):
    # we get as pivot the last element
    pvt = array[last]
    # the index of the last element < pvt found
    min_idx = first - 1
    for i in xrange(first, last):
        # We move all the elements < pvt at the most left position,
        # marked by the min_idx
        if array[i] <= pvt:
            min_idx = min_idx + 1
            array[i], array[min_idx] = array[min_idx], array[i]
    # put pivot in the right position, next the set of min values
    array[min_idx + 1], array[last] = array[last], array[min_idx + 1]
    # return the pivot index
    return min_idx + 1
