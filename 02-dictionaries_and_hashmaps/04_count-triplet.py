
#!/bin/python3
# -----------------------------------------------------------------------------
#! Count Triplets (HackerRank)
#
#! Problem
#   You are given an array `arr` and a number `r`. Count the number of index
#   triplets (i, j, k) with i < j < k such that (arr[i], arr[j], arr[k]) form a
#   geometric progression with common ratio r:
#       arr[j] = arr[i] * r
#       arr[k] = arr[j] * r  (⇒ arr[k] = arr[i] * r^2)
#
#! Example
#   arr = [1, 4, 16, 64], r = 4
#   Triplets: [1,4,16] at indices (0,1,2) and [4,16,64] at (1,2,3)
#   Answer: 2
#
#! Function Description
#   Complete the function:
#       countTriplets(arr: List[int], r: int) -> int
#   Returns the number of valid triplets.
#
#! Input Format
#   - First line: two space-separated integers n and r
#   - Second line: n space-separated integers arr[i]
#
#! Returns
#   - int: number of triplets (may be large; Python int is unbounded)
#
#! Constraints
#   - 1 ≤ n ≤ 10^5
#   - 1 ≤ r ≤ 10^9
#   - 1 ≤ arr[i] ≤ 10^9
#
# Sample Input 0
#   4 2
#   1 2 2 4
# Sample Output 0
#   2
# Explanation 0
#   Valid triplets indices: (0,1,3) → [1,2,4] and (0,2,3) → [1,2,4]
#
# Sample Input 1
#   6 3
#   1 3 9 9 27 81
# Sample Output 1
#   6
# Explanation 1
#   Valid triplets indices:
#     (0,1,2), (0,1,3), (1,2,4), (1,3,4), (2,4,5), (3,4,5)
#
# Sample Input 2
#   5 5
#   1 5 5 25 125
# Sample Output 2
#   4
# Explanation 2
#   Valid triplets indices:
#     (0,1,3), (0,2,3), (1,3,4), (2,3,4)
#
# Typical Approach Hint (for your notes)
#   - Use two hash maps while scanning left→right:
#       left[x]   = count of value x seen so far
#       right[x]  = count of value x remaining to the right (initialized from arr)
#   - For each middle value `m = arr[j]`, the number of triplets centered at j is:
#       left[m/r] * right[m*r]   (only when r == 1 or m % r == 0)
#   - Update maps as you move j.
#   - Time: O(n), Space: O(n)
# -----------------------------------------------------------------------------


#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # variables
    leftdict = defaultdict(int)
    rightdict = defaultdict(int)
    
    # start from left -> need to set the rightdict to be full
    for x in arr:
        rightdict[x] += 1
        
    triplets = 0
    
    for m in arr:
        rightdict[m] -= 1 # moving to the right one by one
        
        # check only availables
        if r == 1:
            triplets += leftdict[m]*rightdict[m]
            
        elif (m % r==0):
            a = m//r
            c = m*r
            
            triplets += leftdict[a]*rightdict[c]
            
        leftdict[m] += 1
            
    return triplets
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
