from collections import deque


def solution(priorities, location):
    count = 0
    while location >= 0:
        if has_upper_priority(priorities):
            tmp = priorities.pop(0)
            priorities.append(tmp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            priorities.pop(0)
            count += 1
            location -= 1

    return count


def has_upper_priority(priorities):
    curr = priorities[0]
    if any(curr < p for p in priorities[1:]):
        return True

    return False


# ===================================


def solution(priorities, location):
    res = 0
    q = deque([(i, p) for i, p in enumerate(priorities)])

    while True:
        cur = q.popleft()
        if any(cur[1] < tup[1] for tup in q):
            q.append(cur)
        else:
            res += 1
            if cur[0] == location:
                return res
