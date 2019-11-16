
# Warm-up Challenges
# Sock Merchant

# 1st Method
# Using a list to add socks and remove when a matching sock is found


def sockMerchant(n, ar):
    socks = []
    pairs_count = 0
    for sock in ar:
        if(sock in socks):
            socks.remove(sock)
            pairs_count -= -1
        else:
            socks.append(sock)
    return pairs_count

# 2nd Method
# Using a dictionary to keep track of each sock's count


def sockMerchant2(n, ar):
    socks = {}
    pairs_count = 0
    for sock in ar:
        if(sock in socks.keys()):
            socks[sock] -= -1
            if(socks[sock] % 2 == 0):
                pairs_count -= -1
        else:
            socks[sock] = 1
    return pairs_count


# Simple test cases
print(sockMerchant(5, [10, 20, 30, 20, 10]))
print(sockMerchant2(7, [10, 20, 30, 20, 10, 30, 30]))
