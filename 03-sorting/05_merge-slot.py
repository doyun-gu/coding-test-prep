# ------------------------------------------------------------
# Problem: Count Inversions
# ------------------------------------------------------------
# In an array arr, a pair of indices (i, j) with i < j is an
# inversion if arr[i] > arr[j]. Inversions are “out-of-order”
# pairs. The minimum number of adjacent swaps needed to sort
# the array equals the number of inversions.
#
# Example
#   arr = [2, 4, 1]
#   Inversions: (2,1), (4,1)  -> answer = 2
#
# Task
#   Implement: countInversions(arr: list[int]) -> int
#   Return the number of inversions in arr.
#
# Input (online judge style)
#   d               # number of datasets
#   n               # size of arr for dataset 1
#   a1 a2 ... an    # the array
#   n               # size of arr for dataset 2
#   ...
#
# Output
#   For each dataset, print the inversion count.
#
# Sample Input
#   2
#   5
#   1 1 1 2 2
#   5
#   2 1 3 1 2
#
# Sample Output
#   0
#   4
#
# Notes / Constraints
#   - 1 <= d <= 15
#   - 1 <= n <= 1e5
#   - Values can be large (e.g., up to 1e7), and duplicates exist.
#   - The answer may not fit in 32-bit; use Python int (unbounded).
#
# Recommended Approach (O(n log n))
#   Use merge sort and, during merge, count "cross inversions":
#   when taking an element from the right half before left half,
#   it forms inversions with all remaining elements in the left half.
#
# Alternative Approaches
#   - Fenwick Tree (BIT) with coordinate compression: O(n log n)
#   - Naive double loop: O(n^2)  (too slow for n up to 1e5)
# ------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Length
    n = len(arr)
    
    if n <= 1:
        return 0
        
    # Create buffer to store value in sorted arr temporarily
    buffer = [0] * n
    
    def processor (leftmost, rightmost):
        
        if leftmost >= rightmost:
            return 0
        
        length = leftmost + rightmost
        mid_pos = length // 2
        
        # Left part
        inv = processor(leftmost, mid_pos)
        # Right part
        inv += processor(mid_pos+1, rightmost)
        # Merge
        inv += merge(leftmost, mid_pos, rightmost)
        
        return inv
        
    def merge (leftmost, mid_pos, rightmost):
        i, j, k = leftmost, mid_pos+1, leftmost
        invCounter = 0
        
        # LEFT -> MID 
        # MID+1 -> RIGHT
        while i<=mid_pos and j<=rightmost:
            # if left is smaller than right
            if arr[i] <= arr[j]:
                buffer[k] = arr[i]
                i += 1
            # left >= right -> All elements will be inversed
            else:
                buffer[k] = arr[j]
                j += 1
                invCounter += (mid_pos - i + 1)
            
            # Move to the next  
            k += 1
        
        # Copy left values in either one left in left or right sided array to the buffer 
        # Left part
        while i <= mid_pos:
            buffer[k] = arr[i]
            i += 1
            k += 1
        # Right part
        while j <= rightmost:
            buffer[k] = arr[j]
            j += 1
            k += 1
            
        # Copy output buffer value in array
        arr[leftmost:rightmost+1] = buffer[leftmost:rightmost+1]
        return invCounter
        
    return processor(0, n-1)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
