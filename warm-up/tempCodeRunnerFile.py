
import math
import sys
from collections import counter

def sockMerchant (n, ar):
    colour_count = counter(ar)
    pairs = 0

    for count in colour_count.values():
        pairs = pairs + count // 2

    return pairs