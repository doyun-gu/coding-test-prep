
#! Problem: Minimum Swaps 2
#
# You are given an array arr which is a permutation of integers [1, 2, ..., n]
# (no duplicates). You are allowed to swap any two elements.
# Find the minimum number of swaps required to sort the array in ascending order.
#
# ---
#! Function
#   minimumSwaps(arr: List[int]) -> int
#
#! Parameters
#   - arr[n]: an unordered array of integers from 1..n (unique, no duplicates)
#
#! Returns
#   - int: the minimum number of swaps to sort the array in ascending order
#
# ---
#! Input Format
#   - First line: integer n, the size of the array
#   - Second line: n space-separated integers, the array arr
#
#! Constraints
#   - 1 <= n <= 10^5 (typically)
#   - arr is a permutation of 1..n (no duplicates)
#
# ---
# Sample Input 0
# 4
# 4 3 1 2
#
# Sample Output 0
# 3
#
# Explanation 0
# Initial: [4, 3, 1, 2]
# swap(0,2) -> [1, 3, 4, 2]
# swap(1,3) -> [1, 2, 4, 3]
# swap(2,3) -> [1, 2, 3, 4]
# Total = 3 swaps.
#
# ---
# Sample Input 1
# 5
# 2 3 4 1 5
#
# Sample Output 1
# 3
#
# Explanation 1
# [2,3,4,1,5] -> [1,3,4,2,5] -> [1,2,4,3,5] -> [1,2,3,4,5]
#
# ---
# Sample Input 2
# 7
# 1 3 5 2 4 6 7
#
# Sample Output 2
# 3
#
# Explanation 2
# [1,3,5,2,4,6,7] -> [1,2,5,3,4,6,7] -> [1,2,3,5,4,6,7] -> [1,2,3,4,5,6,7]
#
# ---
#! Approach Notes
# - This is a "cycle decomposition" problem.
# - For each index i, the correct element should be at position (arr[i] - 1).
# - Using a visited array, detect cycles:
#     A cycle of length k requires (k - 1) swaps.
# - Total minimum swaps = Σ (cycle length - 1) for all cycles.
# - Alternatively, use index-value mapping and swap elements directly into
#   their correct positions (O(n) time).

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    current_index = 0
    end_index = len(arr)
    swap_count = 0
    
    while current_index < end_index:
        correct_index = arr[current_index]-1
        
        if arr[current_index] != arr[correct_index]:
            arr[current_index], arr[correct_index] = arr[correct_index], arr[current_index]
            swap_count = swap_count + 1
            
        else:
            current_index = current_index + 1
    
    return swap_count
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
