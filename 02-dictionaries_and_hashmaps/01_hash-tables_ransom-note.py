
#! Problem: Ransom Note (Dictionaries & Hashmaps)
#
# Harold wrote a ransom note and wants to know if he can recreate it by cutting
# whole words from a magazine. Words are **case-sensitive** and he can only use
# **whole words** (no substrings or concatenation). Each magazine word can be
# used **at most once**.
#
#! Task:
#   Given two word lists — `magazine` and `note` — print "Yes" if the note can
#   be formed exactly using the magazine words; otherwise print "No".
#
# ---
#! Function
#   checkMagazine(magazine: List[str], note: List[str]) -> None
#   (Prints "Yes" or "No"; does not return a value)
#
# ---
#! Input Format
#   Line 1: two space-separated integers m and n (word counts)
#   Line 2: m space-separated strings → magazine words
#   Line 3: n space-separated strings → note words
#
#! Constraints (from the screenshot)
#   1 ≤ m, n ≤ 30000
#   1 ≤ length of each word ≤ 5
#   Words use English letters only (a..z, A..Z)
#
# ---
#! Example
#   magazine = "give me one grand today night"
#   note     = "give one grand today"
#   Output   = "Yes"
#
#   magazine = "two times three is not four"
#   note     = "two times two is four"
#   Output   = "No"   # "two" appears only once in the magazine
#
#   magazine = "ive got a lovely bunch of coconuts"
#   note     = "ive got some coconuts"
#   Output   = "No"   # "some" is missing
#
# ---
#! Approach (using a dictionary / hashmap)
#   1) Count how many times each word appears in the magazine. (frequency map)
#   2) For each word in the note, decrement that count.
#   3) If any word's count goes below 0 (missing/insufficient), print "No".
#   4) If all words satisfied, print "Yes".
#
#   Time:  O(m + n)
#   Space: O(U) where U = number of unique magazine words
#
# ---
#! Reference implementation (both with and without Counter)
#
# Using collections.Counter (short & clear):
#
# from collections import Counter
# def checkMagazine(magazine, note):
#     counts = Counter(magazine)
#     for w in note:
#         counts[w] -= 1
#         if counts[w] < 0:
#             print("No")
#             return
#     print("Yes")
#
# Without Counter (plain dict):
#
# def checkMagazine(magazine, note):
#     counts = {}
#     for w in magazine:
#         counts[w] = counts.get(w, 0) + 1
#     for w in note:
#         if counts.get(w, 0) == 0:
#             print("No")
#             return
#         counts[w] -= 1
#     print("Yes")
#
# -----------------------------------------------------------------------------
#! Mini-Primer: Dictionaries & Hashmaps (Python)
#
# What is a hashmap?
#   - A data structure that maps a *key* to a *value* using a hash function.
#   - Average O(1) time for insert / lookup / update.
#
# Python’s dictionary (`dict`) is a hashmap:
#   d = {}                                 # create
#   d["apple"] = 3                         # insert/update
#   n = d.get("apple", 0)                  # lookup with default (0 if missing)
#   "apple" in d                           # membership check (True/False)
#   for key, value in d.items(): ...       # iterate pairs
#
# When do we use it in coding interviews?
#   - Counting frequencies (words, characters, numbers)
#   - Checking existence / duplicates
#   - Mapping one thing to another (value → index, char → count, etc.)
#
# For this problem:
#   - Keys   = words (strings)
#   - Values = counts (how many times available)
#   - We decrement as we "use" a word for the note.
#
# Tips:
#   - Case-sensitive: "Attack" != "attack".
#   - Don’t return; **print** exactly "Yes"/"No" as required.

#! HACKERRANK ----------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    word_counts={}
    
    # Count all words in magazine and save them in word_counts dict
    for word in magazine:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    # check each word from note exists in magazine
    # Print "No" if there's no
    # Print "Yes" if all words exist
    for word in note:
        if word_counts.get(word, 0) == 0:
            print ("No")
            return
            
        word_counts[word] -= 1
        
    print("Yes")
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
