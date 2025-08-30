
#! Jumping on the Clouds
#! Problem: Jumping on the Clouds
#
# A new mobile game starts with consecutively numbered clouds. 
# Some clouds are safe (cumulus, represented as 0) and others are thunderheads (represented as 1).
#
# The player starts at the first cloud (index 0) and must reach the last cloud.
# Rules:
# - The player can jump from cloud i to cloud i+1 or i+2.
# - The player can only land on safe clouds (0).
# - It is always possible to win the game.
#
#! Task:
# Determine the minimum number of jumps required to get from the start to the last cloud.
#
# ---
#
# Function Description
# --------------------
# Complete the function:
#     jumpingOnClouds(c: List[int]) -> int
#
# Parameters:
# - int c[n]: an array of binary integers (0 = safe, 1 = thunderhead)
#
# Returns:
# - int: the minimum number of jumps required to win the game
#
# ---
#
# Input Format
# ------------
# - The first line contains an integer n, the total number of clouds.
# - The second line contains n space-separated binary integers (0 or 1).
#
# Constraints
# ------------
# - 2 <= n <= 100
# - c[i] ∈ {0, 1}
# - c[0] = c[n-1] = 0 (first and last clouds are always safe)
#
# ---
#
# Output Format
# -------------
# - Print the minimum number of jumps needed to win the game.
#
# ---
#
# Sample Input 0
# --------------
# 7
# 0 0 1 0 0 1 0
#
# Sample Output 0
# ---------------
# 4
#
# Explanation 0
# -------------
# The player must avoid clouds at indices 2 and 5.
# Possible path: 0 → 1 → 3 → 4 → 6
# Total jumps = 4
#
# ---
#
# Sample Input 1
# --------------
# 6
# 0 0 0 0 1 0
#
# Sample Output 1
# ---------------
# 3
#
# Explanation 1
# -------------
# The only thundercloud to avoid is at index 4.
# Path: 0 → 2 → 3 → 5
# Total jumps = 3

def jumpingOnClouds(c):
    current_cloud = 0
    jump_count = 0

    while current_cloud < len(c) - 1:
        if current_cloud + 2 < len(c) and c[current_cloud + 2] == 0:
            current_cloud += 2
        else:
            current_cloud += 1
        jump_count += 1

    return jump_count

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    current_cloud = 0
    jump = 0
    
    while current_cloud < len(c) - 1:
        if current_cloud + 2 <= len(c) - 1 and c[current_cloud + 2] == 0:
            current_cloud = current_cloud + 2
        
        else:
            current_cloud = current_cloud + 1
        jump = jump + 1
            
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
