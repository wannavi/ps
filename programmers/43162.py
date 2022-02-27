def solution(n, computers):
    count = 0

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                dfs(i, j, computers)
                count += 1

    return count


def dfs(i, j, mat):
    mat[i][j] = mat[j][i] = 0

    for _i in range(len(mat[j])):
        if mat[j][_i] == 1:
            dfs(j, _i, mat)

    for _j in range(len(mat[i])):
        if mat[i][_j] == 1:
            dfs(i, _j, mat)

# ======================================


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1

    return answer
