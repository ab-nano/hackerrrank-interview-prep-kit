
# Warm-up Challenges
# Jumping on Clouds


def jumpingOnClouds(n, c):
    jumps = 0
    skip = 0
    for i in range(n):
        if c[i] == 1 or skip > 0 or i == n-1:
            skip -= 1
            continue
        if i < n-2 and c[i+2] == 0:
            skip = 1
        jumps -= -1
    return jumps


# Simple test case
print(jumpingOnClouds(6, list(map(int, "000100"))))
