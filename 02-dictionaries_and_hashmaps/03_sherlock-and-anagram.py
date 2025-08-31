
#! Sherlock and Anagrams (Problem Notes)
#
#! Definition
# - Two strings are anagrams if the letters of one can be rearranged to form the other.
# - Given a string s, count the number of unordered pairs of substrings of s that are anagrams
#   of each other.
#
#! Function
#   sherlockAndAnagrams(s: str) -> int
#! Return
#   The number of unordered anagrammatic substring pairs in s.
#
#! Input Format
#   - The first line contains an integer q, the number of queries.
#   - Each of the next q lines contains a single lowercase string s.
#
#! Constraints
#   - s consists only of lowercase English letters (ascii[a–z]).
#
# Sample Input 0
#   2
#   abba
#   abcd
# Sample Output 0
#   4
#   0
# Explanation 0
#   For "abba":
#     length 1: ('a','a'), ('b','b') → 2 pairs
#     length 2: ('ab','ba'), ('bb','bb') → 2 pairs
#   Total = 4.
#   For "abcd": no letters repeat → 0 pairs.
#
# Sample Input 1
#   2
#   ifailuhkqq
#   kkkk
# Sample Output 1
#   3
#   10
# Explanation 1
#   - In "ifailuhkqq", there are 3 anagrammatic pairs across various lengths.
#   - In "kkkk":
#       length 1: 4 substrings "k" → C(4,2) = 6 pairs
#       length 2: 3 substrings "kk" → C(3,2) = 3 pairs
#       length 3: 2 substrings "kkk" → C(2,2) = 1 pair
#       length 4: 1 substring "kkkk" → 0 pairs
#     Total = 6 + 3 + 1 + 0 = 10.
#
# Sample Input 2
#   1
#   cdcd
# Sample Output 2
#   5
# Explanation 2
#   length 1: 'c' with 'c', and 'd' with 'd' → 2 pairs
#   length 2: anagram pairs among "cd" and "dc" positions → 3 pairs
#   Total = 5.
#
# Approach Hint (typical solution)
#   1) For each length L = 1..len(s), generate all substrings of length L.
#   2) Convert each substring to a canonical “signature” to detect anagrams.
#      Common signatures:
#        - Sorted characters, e.g., sorted("cda") → "acd"
#        - Or a 26-length frequency tuple for O(1) comparison per length.
#   3) Count frequencies of each signature. If a signature occurs k times,
#      it contributes C(k, 2) = k*(k-1)/2 pairs.
#   4) Sum across all lengths.
#
# Complexity (high level)
#   - O(n^2) substrings overall; signature building either O(L log L) by sorting
#     or O(26) using letter counts (preferred).

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    from collections import defaultdict
    
    length = len(s)
    counter_dict = defaultdict(int)
    
    # Count Start Character
    for start_ch in range(length):
        for end_ch in range (start_ch+1, length+1):
            signature = ''.join(sorted(s[start_ch:end_ch]))
            counter_dict[signature] += 1
            
    # Calculate
    total_number = 0
    
    for phrase in counter_dict.values():
        total_number += phrase*(phrase-1)//2
        
    return total_number
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
