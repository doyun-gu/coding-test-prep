
#! Problem: Array Left Rotation
#
# A left rotation operation on an array shifts each element of the array
# one unit to the left. The element at the lowest index moves to the highest index.
# This is also called a circular array shift.
#
#! Example of rotations:
# [1, 2, 3, 4, 5] 
#   → [2, 3, 4, 5, 1]   (after 1 left rotation)
#   → [3, 4, 5, 1, 2]   (after 2 left rotations)
#   → [4, 5, 1, 2, 3]   (after 3 left rotations)
#   → [5, 1, 2, 3, 4]   (after 4 left rotations)
#
# ---
#
#! Function Description
# --------------------
# Complete the function:
#     rotLeft(a: List[int], d: int) -> List[int]
#
# Parameters:
# - int a[n]: the array to rotate
# - int d: the number of left rotations
#
# Returns:
# - int[n]: the rotated array
#
# ---
#
# Input Format
# ------------
# - The first line contains two space-separated integers:
#   n (size of array) and d (number of left rotations).
# - The second line contains n space-separated integers (elements of array a).
#
# Constraints
# ------------
# - 1 <= n <= 10^5
# - 1 <= d <= n
# - 1 <= a[i] <= 10^6
#
# ---
#
# Sample Input
# ------------
# 5 4
# 1 2 3 4 5
#
# Sample Output
# -------------
# 5 1 2 3 4
#
# Explanation
# ------------
# Starting array: [1, 2, 3, 4, 5]
# After 1st left rotation: [2, 3, 4, 5, 1]
# After 2nd left rotation: [3, 4, 5, 1, 2]
# After 3rd left rotation: [4, 5, 1, 2, 3]
# After 4th left rotation: [5, 1, 2, 3, 4]
#
# So the final array is [5, 1, 2, 3, 4].

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    n = len(a)        # length of the array
    d = d % n         # in case d is larger than n (full rotations have no effect)
    return a[d:] + a[:d]  # slice at d and concatenate


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
