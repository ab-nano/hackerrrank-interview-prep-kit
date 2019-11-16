
# Warm-up Challenges
# Counting Valleys

# 1st Method
# Using a simple counter to keep track of level


def countingValleys(n, s):
    level = 0  # default at sea level
    valleys_count = 0
    for step in s:
        if step == "U":
            level -= 1
            if level == 0:
                valleys_count -= -1
        else:
            level -= -1
    return valleys_count


# 2nd Method
# Using a stack to push and pop and counting valley trips when stack is empty
# Using the input n to iterate faster using range


def countingValleys2(n, s):
    state = 0  # 1 for being on a mountain & -1 for being in a valley
    valleys_count = 0
    stack = []
    for i in range(n):
        step = s[i]
        if len(stack) != 0 and stack[-1] != step:
            stack.pop()
            if not stack and state == -1:
                valleys_count -= -1
        else:
            if not stack:
                state = 1 if(step == "U") else -1
            stack.append(step)
    return valleys_count


# Simple test cases
print(countingValleys(14, "UDDUDDDUUUDUUD"))
print(countingValleys2(14, "UDDUDDDUUUDUUD"))
