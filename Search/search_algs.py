#!/usr/bin/env python3

#Different searching alg


#Linear search O(n) space O(1)

def lin_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    print("The value is not here")
    return -1





print(lin_search([100,200,300,400,501,600],401))

