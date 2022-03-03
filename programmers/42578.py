from collections import defaultdict


def solution(clothes):
    dic = defaultdict(int)
    for _, k in clothes:
        dic[k] += 1

    ret = 1
    for v in dic.values():
        ret *= v + 1

    return ret - 1
