
# -----------------------------------------------------------------------------
#! Bubble Sort Problem (HackerRank)
#
# Given an array of integers, sort the array in ascending order using the
# Bubble Sort algorithm. Once sorted, print the following three lines:
#
#   Array is sorted in numSwaps swaps.
#   First Element: firstElement
#   Last Element: lastElement
#
# where:
#   - numSwaps is the number of swaps that took place during the sort
#   - firstElement is the first element in the sorted array
#   - lastElement is the last element in the sorted array
#
#! Example:
#   Initial array: [6, 4, 1]
#   Steps:
#     1) swap(6,4) -> [4,6,1]
#     2) swap(6,1) -> [4,1,6]
#     3) swap(4,1) -> [1,4,6]
#   Total swaps = 3
#
#   Output:
#     Array is sorted in 3 swaps.
#     First Element: 1
#     Last Element: 6
#
#! Function Description
#   Complete the function:
#       def countSwaps(a):
#   Parameters:
#       - a (list[int]): the array of integers to sort
#   Prints:
#       - The three required lines (see above). No return value.
#
#! Input Format
#   - First line: integer n (size of array)
#   - Second line: n space-separated integers (the array elements)
#
#! Constraints
#   - 2 ≤ n ≤ 600
#   - 1 ≤ a[i] ≤ 2 × 10^6
#
# Sample Input 0
#   3
#   1 2 3
# Sample Output 0
#   Array is sorted in 0 swaps.
#   First Element: 1
#   Last Element: 3
#
# Sample Input 1
#   3
#   3 2 1
# Sample Output 1
#   Array is sorted in 3 swaps.
#   First Element: 1
#   Last Element: 3
# -----------------------------------------------------------------------------

##! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    counter = 0
    n = len(a)
    
    for i in range (0, n, 1):
        for j in range (0, n-1, 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
                
    first = a[0]
    last = a[n-1]
                
    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {first}")
    print(f"Last Element: {last}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
