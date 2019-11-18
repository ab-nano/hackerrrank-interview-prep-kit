
# Array Challenges
# Hour Glass Sum

import math

# Calculating the sums by traversing the needed indices in the 2D array and updating the maximum sum so far


def hourglassSum(arr):

    max_sum = - math.inf
    for j in range(4):
        for i in range(4):
            total = arr[j][i]+arr[j][i+1]+arr[j][i+2] + \
                arr[j+1][i+1]+arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
            if total > max_sum:
                max_sum = total
    return max_sum


arr = [[0, -4, -6, 0, -7, -6],
       [-1, -2, -6, -8, -3, -1],
       [-8, -4, -2, -8, -8, -6],
       [-3, -1, -2, -5, -7, -4],
       [-3, -5, -3, -6, -6, -6],
       [-3, -6, 0, -8, -6, -7]]
print(hourglassSum(arr))
