def solution(n, a, b):
    round = 1
    players = [k for k in range(1, n + 1)]  # [1, 2, ... n]

    while len(players) > 1:
        next = []
        for i in range(0, len(players), 2):
            p1, p2 = players[i], players[i + 1]
            if (p1 == a and p2 == b) or (p1 == b and p2 == a):
                return round
            else:
                if p1 == a or p1 == b:
                    next.append(p1)
                elif p2 == a or p2 == b:
                    next.append(p2)
                else:
                    next.append(p1)

        players = next
        round += 1

    return round
