
#! Problem: Array Manipulation
#
# Start with a 1-indexed array of zeros of length n.
# You are given q operations (queries). Each query has three integers: a, b, k.
# For each query, add k to every element in the array from index a to index b (inclusive).
# After applying all queries, return the maximum value in the array.
#
# ---
#! Function
#   arrayManipulation(n: int, queries: List[List[int]]) -> int
#
# Parameters
#   - n: number of elements (array is 1-indexed: positions 1..n)
#   - queries: a 2D list where each item is [a, b, k]
#
# Returns
#   - int: the maximum value in the array after all operations
#
# ---
#! Example (from the screenshot)
#   n = 10
#   queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
#
#   Queries are interpreted as:
#       a b k
#       1 5 3
#       4 8 7
#       6 9 1
#
#   Apply each:
#   - Add 3 to indices 1..5
#   - Add 7 to indices 4..8
#   - Add 1 to indices 6..9
#
#   (Screenshot progression)
#   After 1st: [3,3,3,3,3,0,0,0,0,0]
#   After 2nd: [3,3,3,10,10,7,7,7,0,0]
#   After 3rd: [3,3,3,10,10,8,8,8,1,0]
#   Max = 10
#
# ---
# Sample Input
#   5 3
#   1 2 100
#   2 5 100
#   3 4 100
#
# Sample Output
#   200
#
# Explanation
#   Start: [0, 0, 0, 0, 0]
#   After [1,2,100]: [100,100,  0,  0,  0]
#   After [2,5,100]: [100,200,100,100,100]
#   After [3,4,100]: [100,200,200,200,100]
#   Max = 200
#
# ---
# Constraints
#   - 1 <= n <= 10^7 (large!)
#   - 1 <= q <= 2 * 10^5
#   - 1 <= a <= b <= n
#   - 0 <= k <= 10^9
#
# ---
#! Performance Note (typical approach)
#   Directly updating every index in [a..b] for each query is O(n*q) and will time out.
#   Use a difference array (prefix sum trick):
#     diff[a]   += k
#     diff[b+1] -= k   (if b+1 <= n)
#   Then take a running prefix sum over diff to rebuild final values and track the max.
#   Time: O(n + q), Space: O(n)

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    #create general & differential array
    # arr=[0]*n <- No need for this question
    diff_arr=[0]*(n+2)
    
    # Make differential Array
    for a, b, k in queries:
        # Differential Array start & end point
        diff_arr[a-1] += k
        diff_arr[b] -= k
        
    # Add prefixsum
    prefixsum = 0
    max_value = 0
    
    for i in range (0, n):
        prefixsum += diff_arr[i]
        # arr[i] = prefixsum
        
        if prefixsum > max_value:
            max_value = prefixsum
    
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
