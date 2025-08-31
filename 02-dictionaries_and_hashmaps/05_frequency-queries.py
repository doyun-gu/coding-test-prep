
# -----------------------------------------------------------------------------
#! Frequency Queries (HackerRank)
#
#! Problem
#   You are given q queries. Each query is a pair (op, val):
#     1 x : Insert value x into the data structure.
#     2 y : Delete ONE occurrence of value y, if present.
#     3 z : Check if there exists ANY value whose frequency is exactly z.
#           Output 1 if yes, else 0.
#
#   Queries are given as a 2-D array `queries` of size q where:
#     - queries[i][0] is the operation type (1, 2, or 3)
#     - queries[i][1] is the associated value
#
#! Example
#   queries = [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]
#   Outputs for type-3 queries: [0, 1]
#
#! Function Description
#   Complete:
#       def freqQuery(queries: list[list[int]]) -> list[int]
#   Return a list with the results for each type-3 query, in order.
#
#! Input Format
#   - First line: integer q (number of queries)
#   - Next q lines: two space-separated integers: queries[i][0], queries[i][1]
#
#! Returns
#   - list[int]: results of all type-3 queries (each either 0 or 1)
#
#! Constraints
#   - 1 ≤ q ≤ 10^5
#   - 1 ≤ x, y, z ≤ 10^9
#   - queries[i][0] ∈ {1, 2, 3}
#
# Sample Input 0
#   8
#   1 5
#   1 6
#   3 2
#   1 10
#   1 10
#   1 6
#   2 5
#   3 2
#
# Sample Output 0
#   0
#   1
#
# Explanation 0
#   After some operations, when asked "is there a value with frequency 2?",
#   the answers are 0 then 1.
#
# Sample Input 1
#   4
#   3 4
#   2 1003
#   1 16
#   3 1
#
# Sample Output 1
#   0
#   1
#
# Sample Input 2
#   10
#   1 3
#   2 3
#   3 2
#   1 4
#   1 5
#   1 4
#   3 2
#   2 4
#   3 2
#
# Sample Output 2
#   0
#   1
#   1
#
# Typical Approach Hint (O(q) time)
#   Maintain two hash maps:
#     - freq_of_val[v] = current frequency of value v
#     - count_of_freq[f] = how many distinct values currently appear exactly f times
#   For op 1 (insert x):
#     old = freq_of_val[x]; new = old + 1
#     decrement count_of_freq[old], increment count_of_freq[new]
#   For op 2 (delete y if present):
#     if old = freq_of_val[y] > 0:
#         new = old - 1
#         decrement count_of_freq[old], increment count_of_freq[new]
#   For op 3 (check z):
#     append 1 if count_of_freq[z] > 0 else 0
#   This makes type-3 queries O(1) without scanning values.
# -----------------------------------------------------------------------------

# TODO: implement the function body.
def freqQuery(queries):
    """
    queries: list of [op, val]
    return: list of ints (answers to op==3)
    """
    # Implement using two dicts as described above.
    # freq_of_val = {}
    # count_of_freq = {}
    # ans = []
    # for op, x in queries:
    #     if op == 1:
    #         ...
    #     elif op == 2:
    #         ...
    #     else:  # op == 3
    #         ans.append(1 if count_of_freq.get(x, 0) > 0 else 0)
    # return ans
    pass

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    freqVal = defaultdict(int) 
    freqCount = defaultdict(int)
    ans = []
    
    for op, v in queries:
        if op == 1:
            old = freqVal[v]
            new = old + 1
            freqVal[v] = new
            
            if old > 0:
                freqCount[old] -= 1
            freqCount[new] += 1
            
        elif op == 2:
            old = freqVal[v]
            
            if old > 0:
                new = old -1
                freqVal[v] = new
                freqCount[old] -= 1
                
                if new > 0:
                    freqCount[new] += 1
            
        else:
            ans.append(1 if freqCount[v] > 0 else 0)
            
    return ans
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
