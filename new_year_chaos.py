
# Array Challenges
# New Year Chaos Challenge

# A solution with two loops that times out with huge test cases


def minimumBribes(q):
    queue_length = len(q)
    bribes_count = 0
    bribers = []
    expected_person = 1
    for i in range(queue_length):
        current_person = q[i]
        position_difference = current_person - (i+1)
        if position_difference > 2:
            bribes_count = "Too chaotic"
            break
        for bribing_person in bribers:
            if current_person < bribing_person:
                bribes_count -= -1
        if current_person == expected_person:
            expected_person -= -1
        else:
            bribers.append(current_person)
    print(bribes_count)


# Test case
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
