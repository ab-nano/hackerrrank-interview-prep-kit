
# Array Challenges
# Array Manipulation

# Method 1
# Efficient Solution. Passes all test cases


def arrayManipulation(n, queries):
    arr = [0]*n
    for operation in queries:
        arr[operation[0]-1] += operation[2]
        if operation[1] < n:
            arr[operation[1]] -= operation[2]
    maxi = 0
    count = 0
    for item in arr:
        count += item
        if count > maxi:
            maxi = count
    return maxi


# Method 2
# double iteration inefficient solution. Timesout for huge test cases


def arrayManipulation2(n, queries):
    arr = [0]*n
    maxi = 0
    for operation in queries:
        for i in range(operation[0], operation[1]+1):
            arr[i-1] += operation[2]
            if arr[i-1] > maxi:
                maxi = arr[i-1]
    print(maxi)


arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
