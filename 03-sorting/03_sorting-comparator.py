
#!/bin/python3
# -----------------------------------------------------------------------------
# Sorting: Comparator (HackerRank)
#
# Problem
#   We are given an array of Player objects.
#   Each Player has two fields:
#       - name: string
#       - score: int
#
#   Requirement:
#     - Sort the list of players in:
#         1) Descending order by score
#         2) If scores are equal → Ascending order by name (alphabetical)
#
#   The problem mimics Java's Comparator interface, but in Python we solve it
#   using custom sort with "key" or functools.cmp_to_key.
#
# Example
#   Input:
#       5
#       amy 100
#       david 100
#       heraldo 50
#       aakansha 75
#       aleksa 150
#
#   Expected Output:
#       aleksa 150
#       amy 100
#       david 100
#       aakansha 75
#       heraldo 50
#
# Functionality
#   - Read n, then read n lines of (name, score).
#   - Create list of Player(name, score).
#   - Sort using comparator:
#       - First: score descending
#       - Then: name ascending
#   - Print sorted list (handled by the provided stub).
#
# Constraints
#   - 0 ≤ score ≤ 1000
#   - Names are lowercase alphabetic
#   - Two or more players can have the same score
#   - Two or more players can have the same name
#
# Output
#   - Sorted list of players (name score) line by line
# -----------------------------------------------------------------------------

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name} {self.score}"
        
    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score
            
        else:
            if a.name < b.name:
                return -1
                
            elif a.name > b.name:
                return 1
                
            else:
                return 0
            

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)