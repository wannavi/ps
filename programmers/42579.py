from collections import defaultdict


def solution(genres, plays):
    res = []
    dic = defaultdict(list)
    total_plays = defaultdict(int)

    for i, (g, p) in enumerate(zip(genres, plays)):
        dic[g].append((p, i))
        total_plays[g] += p

    sorted_genres = [k for k, _ in sorted(
        total_plays.items(), key=lambda x: -x[1])]

    for g in sorted_genres:
        genre_plays = sorted(dic[g], key=lambda x: (-x[0], x[1]))[:2]
        res += [i for _, i in genre_plays]

    return res
