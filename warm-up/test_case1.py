
#! Sales by Match

# There is a large pile of socks that must be paired by colour.
# Given an array of integers representing the colour of each sock, determine how many pairs of socks with matching colours there are.

# Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]

# There is only one pair of colour 1 and one of colour 2.
# There are three odd socks left, one of each colour. The number of pairs is 2.

# Function Description
# Compare the sockMerchant function in the editor below:

# sockMerchant has the following parameters:

# int n: the number of socks in the pile
# int ar[n]: the colours of each sock

# Returns int: the number of pairs of socks with matching colours

# Input Format:
# The first line contains an integer n, the number of socks represented in ar.
# The second line contains n space-separated integers, ar[i], the colours of each sock.

# Constraints:
# 1 <= n <= 100
# 1 <= ar[i] <= 100 where 0 <= i < n

# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# Sample Output
# 3

#! PRACTICE CODE ------------------------------------------------

# Libraries --------------------------------------------------------
import math
import sys
from collections import Counter

# Function --------------------------------------------------------
def sockMerchant (n, ar):
    colour_count = Counter(ar)
    pairs = 0

    for count in colour_count.values():
        pairs = pairs + count // 2

    return pairs

# Input ----------------------------------------------------------------
n = int(input())
ar = list(map(int, input().rstrip().split()))

print(sockMerchant(n, ar))


#! HACKERRANK ----------------------------------------------------

# import math
# import os
# import random
# import re
# import sys

# from collections import Counter

# #
# # Complete the 'sockMerchant' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. INTEGER_ARRAY ar
# #

# def sockMerchant(n, ar):
#     colour_count = Counter(ar)
#     pairs = 0
    
#     for count in colour_count.values():
#         pairs = pairs + count // 2
        
#     return pairs

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
