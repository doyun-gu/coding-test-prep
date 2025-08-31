
#! Counting Valleys
#* Problem: Counting Valleys
#
# An avid hiker keeps meticulous records of their hikes. 
# During the last hike that took exactly `steps` steps, for every step 
# it was noted if it was an uphill (`U`), or a downhill (`D`) step. 
#
# - Hikes always start and end at sea level.
# - Each step up or down represents a unit change in altitude.
#
#* Definitions:
# - A *mountain* is a sequence of consecutive steps **above sea level**, 
#   starting with a step up from sea level and ending with a step down to sea level.
# - A *valley* is a sequence of consecutive steps **below sea level**, 
#   starting with a step down from sea level and ending with a step up to sea level.
#
#* Task:
# - Hikes always start and end at sea level.
# - Each step up or down represents a unit change in altitude.
#
#* Definitions:
# - A *mountain* is a sequence of consecutive steps **above sea level**, 
#   starting with a step up from sea level and ending with a step down to sea level.
# - A *valley* is a sequence of consecutive steps **below sea level**, 
#   starting with a step down from sea level and ending with a step up to sea level.
#
#* Task:
# Given the sequence of up and down steps during a hike, 
# find and print the number of valleys walked through.
#
# ---
#
# Function Description
# --------------------
# Complete the function:
#     countingValleys(steps: int, path: str) -> int
#
# Parameters:
# - int steps: the number of steps on the hike
# - string path: a string describing the path, consisting of 'U' and 'D'
#
# Returns:
# - int: the number of valleys traversed
#
# ---
#
# Input Format
# ------------
# - The first line contains an integer `steps`, the number of steps.
# - The second line contains a string `path` of `steps` characters describing the path.
#
# Constraints
# ------------
# - 2 <= steps <= 10^6
# - path[i] ∈ { 'U', 'D' }
#
# ---
#
# Sample Input
# ------------
# 8
# UDDDUDUU
#
# Sample Output
# -------------
# 1
#
# Explanation
# ------------
# Representing sea level as `_`, uphill as `/`, and downhill as `\`:
#
# _/\      _
#    \    /
#     \/\/
#
# The hiker enters and exits exactly **one valley**.

#! PRACTICE CODE ------------------------------------------------

def countingValleys(steps, path):
    altitude = 0
    valley_count = 0

    for step in path:
        if step == 'U':
            altitude = altitude + 1
            if altitude == 0:
                valley_count = valley_count + 1

        elif step == 'D':
            altitude = altitude - 1

    return valley_count

steps = 8
path = "UDDDUDUU"

print(countingValleys(steps, path))

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valley_count = 0
    
    for step in path:
        if step == 'U':
            altitude = altitude + 1
            if altitude == 0:
                valley_count = valley_count + 1
    
        elif step == 'D':
            altitude = altitude - 1
            
    return valley_count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

