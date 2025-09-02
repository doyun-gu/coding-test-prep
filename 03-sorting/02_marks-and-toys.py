
#!/bin/python3
# -----------------------------------------------------------------------------
# Mark and Toys (HackerRank - Greedy + Sorting)
#
# Problem
#   Mark wants to buy toys for his son. Each toy has a price.
#   Mark has a budget k and wants to maximize the number of toys he can buy.
#   Each toy can be bought at most once.
#
# Example
#   prices = [1, 2, 3, 4], k = 7
#   Options:
#     - Buy [1, 2, 3] for total 6 → 3 toys
#     - Buy [3, 4] for total 7 → 2 toys
#   Maximum = 3
#
# Function Description
#   Complete:
#       def maximumToys(prices, k):
#   Parameters:
#       - prices: list[int], the toy prices
#       - k: int, Mark's budget
#   Returns:
#       - int, the maximum number of toys Mark can buy
#
# Input Format
#   - First line: two integers n, k
#       n = number of toys
#       k = budget
#   - Second line: n space-separated integers, the prices[i]
#
# Constraints
#   - 1 ≤ n ≤ 10^5
#   - 1 ≤ k ≤ 10^9
#   - 1 ≤ prices[i] ≤ 10^9
#   - A toy can't be bought multiple times
#
# Sample Input
#   7 50
#   1 12 5 111 200 1000 10
#
# Sample Output
#   4
#
# Explanation
#   Sort prices → [1, 5, 10, 12, 111, 200, 1000]
#   Buy toys in order until budget exceeded:
#     1 (total=1), 5 (total=6), 10 (total=16), 12 (total=28)
#   Next is 111 → exceeds 50, stop.
#   Maximum = 4 toys
# -----------------------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    prices.sort()
    used = 0
    counter = 0
    
    for price in prices:
        if used + price <= k:
            used += price
            counter += 1
            
        else:
            break
            
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
