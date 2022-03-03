from collections import defaultdict


def solution(p, c):
    dic = defaultdict(int)

    for pp in p:
        dic[pp] += 1

    for cc in c:
        dic[cc] -= 1

    for k, v in dic.items():
        if v != 0:
            return k
