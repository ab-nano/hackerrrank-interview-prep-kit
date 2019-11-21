
# Array Challenges
# New Year Chaos Challenge

# Method 1
# Fastest Solution with the full score using one iteration over the queue and an find index function with a cost less than a nested iteration


def minimumBribes(q):
    queue_length = len(q)
    bribes_count = 0
    expected_sticker = [i for i in range(queue_length, 0, -1)]
    for i in range(queue_length-1, -1, -1):
        current_person = q[i]
        position_difference = current_person - (i+1)
        if position_difference > 2:
            bribes_count = "Too chaotic"
            break
        if current_person == expected_sticker[0]:
            del expected_sticker[0]
        else:
            bribes_count += expected_sticker.index(current_person)
            expected_sticker.remove(current_person)
    print(bribes_count)


# Method 2
# A solution with two loops that times out with huge test cases


def minimumBribes2(q):
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
