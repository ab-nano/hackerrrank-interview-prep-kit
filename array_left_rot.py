
# Array Challenges
# Arrays Left Rotation

# Excluding all the full cyclic number of rotations that gives the same original array and executing the remaining rotations


def rotLeft(n, a, d):
    needed_rotations = d % n
    rotated_elements = []
    for _ in range(needed_rotations):
        rotated_elements.append(a.pop(0))
    return a + rotated_elements


# Test case
print(rotLeft(5, [1, 2, 3, 4, 5], 4))
