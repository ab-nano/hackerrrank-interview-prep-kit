
# Array Challenges
# Array Manipulation

# Method 1
#


def arrayManipulation(maximum, queries):
    maxi = 0
    for i, operation in enumerate(queries):
        operation_start = operation[0]
        operation_end = operation[1]
        operation_value = operation[2]
        for j, comparing_operation in enumerate(queries, start=1):
            comparing_operation_start = comparing_operation[0]
            comparing_operation_end = comparing_operation[1]
            comparing_operation_value = comparing_operation[2]
            # The case where the sets are disjoint
            if comparing_operation_start > operation_end or operation_start > comparing_operation_end:
                next
            # The case where the sets are exactly equivalent
            if comparing_operation_start == operation_start and comparing_operation_end == operation_end:
                new_value = operation_value + comparing_operation_value
                comparing_operation[2] = new_value
                if new_value > maxi:
                    maxi = new_value
                del queries[i]
                break
            # check which operation starts first
            if comparing_operation_start > operation_start:
                # The case where the sets intersect
                if comparing_operation_end > operation_end:
                    queries.append(
                        [operation_start, comparing_operation_start-1, operation_value])

                    comparing_operation[1] = operation_end
                    new_value = operation_value + comparing_operation_value
                    comparing_operation[2] = new_value

                    queries.append(
                        [operation_end+1, comparing_operation_end, comparing_operation_value])

                    if new_value > maxi:
                        maxi = new_value
                    del queries[i]
                    break
                elif comparing_operation_end == operation_end:
                    queries.append(
                        [operation_start, comparing_operation_start-1, operation_value])

                    new_value = operation_value + comparing_operation_value
                    comparing_operation[2] = new_value

                    if new_value > maxi:
                        maxi = new_value

                else:
                    queries.append(
                        [operation_start, comparing_operation_start-1, operation_value])

                    new_value = operation_value + comparing_operation_value
                    comparing_operation[2] = new_value

                    queries.append(
                        [comparing_operation_end+1, operation_end, comparing_operation_value])

                    if new_value > maxi:
                        maxi = new_value

            # elif comparing_operation_start == operation_start:

            # else:

                #
            # if (comparing_operation_start >= operation_start and comparing_operation_end <= operation_end) or
            # (operation_start)


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
