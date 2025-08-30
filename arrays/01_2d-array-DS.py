
#! Problem: 2D Array – Hourglass Sum
#
# An hourglass in a 2D array has the shape:
# a b c
#   d
# e f g
#
# In a 6x6 array there are 16 hourglasses (top-left anchor (i,j) where i,j ∈ [0..3]).
# For each hourglass, compute its sum and return the maximum.
#
# Function
# --------
#     hourglassSum(arr: List[List[int]]) -> int
#
# Parameters
# ----------
# - arr: 6x6 list of integers (can be negative)
#
# Returns
# -------
# - int: maximum hourglass sum found in arr
#
# Example (input grid)
# -9 -9 -9  1  1  1
#  0 -9  0  4  3  2
# -9 -9 -9  1  2  3
#  0  0  8  6  6  0
#  0  0  0 -2  0  0
#  0  0  1  2  4  0
#
# Hourglass sums (16 of them) are computed and the maximum is returned.
#
# Notes
# -----
# - Values can be negative, so initialize the max with a very small number
#   (or the first hourglass sum).
# - Valid hourglass anchors: i = 0..3, j = 0..3.

def hourglassSum(arr):
    max_sum = -float("inf")
    
    for i in range(4):        # row: 0-3
        for j in range(4):    # col: 0-3
            current = (
                arr[i][j]   + arr[i][j+1]   + arr[i][j+2] +
                              arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            if current > max_sum:
                max_sum = current
    return max_sum

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# def hourglassSum(arr):
#     max_sum = -float("inf")
    
#     for i in range(4):        # row: 0-3
#         for j in range(4):    # col: 0-3
#             current = (
#                 arr[i][j]   + arr[i][j+1]   + arr[i][j+2] +
#                               arr[i+1][j+1] +
#                 arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
#             )
#             if current > max_sum:
#                 max_sum = current
#     return max_sum

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = hourglassSum(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
