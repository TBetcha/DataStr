#!/usr/bin/env python3
import math
#Different searching alg


#Linear search O(n) space O(1)

def lin_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    print("The value is not here")
    return -1


# binary search, faster than linear
# works only with sorted elements
# O(logN)

def binary_search(arr, val):
    start = 0
    end = len(arr)-1
    mid = math.floor((start+end)/2)
    while not(arr[mid]==val) and start<=end:
        if val<arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = math.floor((start+end)/2)
    if arr[mid] == val:
        return mid
    else:
        return -1

cust_arr = [ 8, 9, 12 ,15, 16, 19, 20, 21, 28]
print(binary_search(cust_arr, 15))
#print(lin_search([100,200,300,400,501,600],401))

