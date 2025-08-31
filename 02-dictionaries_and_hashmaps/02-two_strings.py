
#! Problem: Two Strings
#
# Given two strings, determine if they share a common substring.
# A substring may be as small as one character.
#
#! Example:
#   s1 = "hello", s2 = "world"
#   → They share 'o' and 'l' → return "YES"
#
#   s1 = "hi", s2 = "world"
#   → They share no characters → return "NO"
#
#! Function Description:
#   Complete the function `twoStrings` with the following parameters:
#
#!   Parameters:
#     string s1: a string
#     string s2: another string
#
#!   Returns:
#     string: either "YES" or "NO"
#
#! Input Format:
#   - The first line contains a single integer p, the number of test cases.
#   - The following p pairs of lines are as follows:
#       * First line: string s1
#       * Second line: string s2
#
#! Constraints:
#   - Both s1 and s2 consist only of lowercase ascii letters (a-z).
#
#! Output Format:
#   - For each pair of strings, print "YES" if they share a common substring,
#     otherwise print "NO".
#
# Sample Input:
#   2
#   hello
#   world
#   hi
#   world
#
# Sample Output:
#   YES
#   NO
#
# Explanation (from image):
#   Test Case 1:
#     s1 = "hello", s2 = "world"
#     Common substrings: "o", "l"
#     → Answer: YES
#
#   Test Case 2:
#     s1 = "hi", s2 = "world"
#     No common characters
#     → Answer: NO

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
