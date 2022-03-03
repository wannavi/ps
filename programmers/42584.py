def solution(prices):
    res = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                res[i] += 1
            else:
                break

    return res
