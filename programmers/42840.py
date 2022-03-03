def solution(answers):
    scores = [0, 0, 0]
    p0 = [1, 2, 3, 4, 5]
    p1 = [2, 1, 2, 3, 2, 4, 2, 5]
    p2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        ans = answers[i]
        if p0[i % len(p0)] == ans:
            scores[0] += 1
        if p1[i % len(p1)] == ans:
            scores[1] += 1
        if p2[i % len(p2)] == ans:
            scores[2] += 1

    best = max(scores)
    return [i + 1 for i, n in enumerate(scores) if n == best]
