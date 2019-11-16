
# Warm-up Challenges
# Repeated String

from __future__ import division
import math


def repeatedString(s, n):
    string_length = len(s)
    a_count = s.count('a')
    repititions = math.floor(n/string_length)
    total_count = a_count*repititions
    final_repetition_string = s[:n % string_length]
    total_count += final_repetition_string.count('a')
    return total_count


# Simple test case
print(repeatedString("aba", 10))
