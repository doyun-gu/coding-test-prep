
#! Repeated String
#
# There is a string `s` of lowercase English letters that is repeated infinitely many times. 
# Given an integer `n`, find and print the number of letter 'a's 
# in the first `n` characters of the infinite string.
#
# ---
#
#! Function Description
# --------------------
# Complete the function:
#     repeatedString(s: str, n: int) -> int
#
#! Parameters:
# - string s: a string to repeat
# - int n: the number of characters to consider
#
#! Returns:
# - int: the frequency of 'a' in the first `n` characters
#
# ---
#
#! Input Format
# ------------
# - The first line contains a single string `s`.
# - The second line contains an integer `n`.
#
#! Constraints
# ------------
# - 1 <= |s| <= 100
# - 1 <= n <= 10^12
# - For 25% of the test cases, n <= 10^6
#
# ---
#
# Sample Input 0
# --------------
# aba
# 10
#
# Sample Output 0
# ---------------
# 7
#
# Explanation 0
# -------------
# The infinite string is: "abaabaabaa..."
# The first 10 characters are "abaabaabaa".
# There are 7 occurrences of 'a' → return 7.
#
# ---
#
# Sample Input 1
# --------------
# a
# 1000000000000
#
# Sample Output 1
# ---------------
# 1000000000000
#
# Explanation 1
# -------------
# Since the string is just "a", 
# all of the first 10^12 characters are 'a'. 
# Answer = 1000000000000.

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

#NOTE This does not work because of the run priority must use the below one.
# def repeatedString(s, n):
#     # Write your code here
#     return s.count('a') * n // len(s) + s[:n % len(s)].count('a')

def repeatedString(s, n):

    # Count how many 'a's are in one full instance of s
    a_in_s = s.count('a')

    # Calculate how many times s fully fits into the first n characters
    full_count = n // len(s)

    # Calculate the leftover characters after the full repeats
    rem_count = n % len(s)

    # Total 'a's = (number of 'a's in full repeats)
    #            + (number of 'a's in the leftover substring)
    return a_in_s * full_count + s[:rem_count].count('a')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
