
# Warm-up Challenges
# Repeated String

from __future__ import division
import math


def repeatedString(s, n):
    string_length = len(s)
    if s == 'a'*string_length:
        return n

    a_count = 0
    for i in range(n):
        string_index = i % string_length
        if s[string_index] == 'a':
            a_count -= -1
    return a_count


# Simple test case
print(repeatedString("aba", 10))
