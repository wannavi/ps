from collections import deque
from collections import Counter


def solution(begin, target, words):
    graph = makeWordGraph([begin, *words])

    # Find shortest path (node ~ node)
    res = []
    discovered = []
    stack = [(begin, 0)]  # (node, depth)
    while stack:
        node, depth = stack.pop()
        for w in graph[node]:
            if w not in discovered:
                discovered.append(w)
                if w == target:
                    res.append(depth + 1)
                else:
                    stack.append((w, depth + 1))

    return min(res) if res else 0


def makeWordGraph(words):
    graph = {word: [] for word in words}

    for word1 in words:
        for word2 in words:
            if isDiffOneChar(word1, word2):
                graph[word1].append(word2)
                graph[word2].append(word1)

    return graph


def isDiffOneChar(word1, word2):
    diff = Counter(word1) - Counter(word2)
    ret = 0
    for v in diff.values():
        if v != 0:
            ret += 1

    return ret == 1


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

# ===============================================


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)
