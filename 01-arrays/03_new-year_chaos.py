
#! Problem: New Year Chaos
#
# It's New Year's Day and people are in line for the Wonderland rollercoaster ride. 
# Each person wears a sticker indicating their initial position in the queue from 1 to n.
#
#! Rules:
# - Any person can bribe the person directly in front of them to swap positions.
# - A person can bribe at most two others.
# - Stickers always stay the same (the original position number).
#
#! Task:
# - Determine the minimum number of bribes that took place to get to a given queue order.
# - If anyone has bribed more than two people, print "Too chaotic".
#
# ---
#
#! Function Description
# --------------------
# Complete the function:
#     minimumBribes(q: List[int]) -> None
#
# Parameters:
# - int q[n]: the positions of the people after all bribes
#
# Returns:
# - No value is returned.
# - Print the minimum number of bribes necessary,
#   or "Too chaotic" if someone has bribed more than 2 people.
#
# ---
#
# Input Format
# ------------
# - The first line contains an integer t, the number of test cases.
# - Each test case has:
#   - One line with an integer n (the number of people in the queue).
#   - One line with n space-separated integers (the final state of the queue).
#
# Constraints
# ------------
# - 1 <= t <= 10
# - 1 <= n <= 10^5
#
# ---
#
# Sample Input
# ------------
# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
#
# Sample Output
# -------------
# 3
# Too chaotic
#
# Explanation
# ------------
# Test Case 1:
# Initial state: [1, 2, 3, 4, 5]
# - Person 5 bribes 4 → [1, 2, 3, 5, 4]
# - Person 5 bribes 3 → [1, 2, 5, 3, 4]
# - Person 2 bribes 1 → [2, 1, 5, 3, 4]
# Total = 3 bribes
#
# Test Case 2:
# Person 5 appears to have bribed more than 2 people.
# This is impossible → "Too chaotic"

def minimumBribes(q):
    for i, x in enumerate(q):
        if x - (i+1) > 2:
            print("Too chaotic")
            return
        
    bribe = 0
    for i, x in enumerate(q):
        start = max(x-2, 1)

        for j in range (start-1, i):
            if q[j] > x:
                bribe += 1

    print(bribe)

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribe_count = 0

    for i, x in enumerate(q):
        # 1) Too chaotic check
        if x - (i + 1) > 2:
            print("Too chaotic")
            return

        # 2) Count bribes: only need to check from max(x-2, 1) up to i-1
        start_index = max(x - 2, 1)
        for j in range(start_index - 1, i):
            if q[j] > x:
                bribe_count += 1

    print(bribe_count)
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
