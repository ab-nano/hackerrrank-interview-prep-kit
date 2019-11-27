
# Array Challenges
# Minimum Swap 2 Challenge

# Method 1
#


def minimumSwaps(arr, index_diff=0):
    if len(arr) == 1:
        return 0
    elif arr[0] == 1 + index_diff:
        return minimumSwaps(arr[1:], index_diff + 1)
    else:
        current_value = arr[0]
        for i in range(len(arr)-1, -1, -1):
            potential_swap = arr[i]
            print(current_value, index_diff+1, potential_swap, i)
            if potential_swap < i + index_diff + 1 and current_value > potential_swap and current_value - potential_swap > i:
                arr[i] = current_value
                if potential_swap == 1+index_diff:
                    return 1 + minimumSwaps(arr[1:], index_diff + 1)
                else:
                    arr[0] = potential_swap
                    return 1 + minimumSwaps(arr, index_diff)


print(minimumSwaps([7, 1, 5, 2, 4, 3, 6]))
