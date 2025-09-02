
#!/bin/python3
# -----------------------------------------------------------------------------
# Fraudulent Activity Notifications (HackerRank)
#
# Problem
#   HackerLand National Bank monitors clients’ spending.
#   Rule: On a given day, if today's expenditure >= 2 * median of the previous d days,
#         send a notification.
#   Bank only starts sending notifications after it has at least d days of prior data.
#
# Example
#   expenditure = [10, 20, 30, 40, 50], d = 3
#   Day 4 → trailing [10,20,30], median=20, today=40 → 40 >= 40 → 1 notification
#   Day 5 → trailing [20,30,40], median=30, today=50 → 50 < 60 → no notification
#   Total = 1
#
# Function Description
#   Complete:
#       def activityNotifications(expenditure, d):
#   Parameters:
#       - expenditure: list[int], daily expenditures
#       - d: int, the lookback window size
#   Returns:
#       - int: number of notifications sent
#
# Input Format
#   - First line: n d (n = number of days, d = lookback window)
#   - Second line: n space-separated integers expenditure[i]
#
# Constraints
#   - 1 ≤ n ≤ 2 * 10^5
#   - 1 ≤ d ≤ n
#   - 0 ≤ expenditure[i] ≤ 200
#
# Output Format
#   - Single integer: number of notifications
#
# Sample Input 0
#   9 5
#   2 3 4 2 3 6 8 4 5
# Sample Output 0
#   2
#
# Explanation
#   First 5 days = collecting data.
#   Day 6 → trailing [2,3,4,2,3], median=3, today=6 → 6 >= 2*3 → +1
#   Day 7 → trailing [3,4,2,3,6], median=3, today=8 → 8 >= 2*3 → +1
#   Day 8 → trailing [4,2,3,6,8], median=4, today=4 → 4 < 2*4 → 0
#   Day 9 → trailing [2,3,6,8,4], median=4, today=5 → 5 < 2*4 → 0
#   Total notifications = 2
#
# Sample Input 1
#   5 4
#   1 2 3 4 4
# Sample Output 1
#   0
#   Because median=2.5, today=4, 4 < 5 → no notification
# -----------------------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Variables
    n = len(expenditure)
    window_size = d
    
    # Check
    if n <= d:
        return 0
        
    # Set windows
    tracker = [0]*201
    
    # Track per amount of spend
    for daily_spend in expenditure[:window_size]:
        tracker[daily_spend] += 1
    
    # Calculate median and return 2*median
    def processor (tracker, window_size):
        counter = 0
        # CASE odd
        if window_size%2 == 1:
            # Find the position
            target_pos = window_size//2 + 1
            
            # Find the Median Value
            for value, count in enumerate(tracker):
                counter += count
                
                if counter >= target_pos:
                    return 2*value
            
            # CASE even -> set window        
        else:
            left_pos = window_size//2
            right_pos = window_size//2+1
            
            left_val = None
            right_val = None
            
            # Left Case
            for value, count in enumerate(tracker):
                counter += count
                
                if left_val == None and counter >= left_pos:
                    left_val = value
                    
                if counter >= right_pos:
                    right_val = value
                    return left_val + right_val
            return 0
            
    notf_counter = 0
    
    for today in range(d, n):
        trigger = processor(tracker, window_size)
        daily_spending = expenditure[today]
        
        if daily_spending >= trigger:
            notf_counter += 1
            
        # Move the window to the right
        wleft_val = expenditure[today-d]     # Left-most value in the window
        wright_val = expenditure[today]      # Right-most value in the window
        
        tracker[wleft_val] -= 1
        tracker[wright_val] += 1
    
    return notf_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
