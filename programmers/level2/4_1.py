def solution(dirs):
    curr = [0, 0]
    paths = []   # [p1, p2], [p1, p3], ...

    # ASC p1 -> p2
    for direction in dirs:
        path = [curr]

        if direction == "L":
            if -5 <= curr[0] - 1 <= 5:
                curr = [curr[0] - 1, curr[1]]
        elif direction == "R":
            if -5 <= curr[0] - 1 <= 5:
                curr = [curr[0] + 1, curr[1]]
        elif direction == "U":
            if -5 <= curr[1] - 1 <= 5:
                curr = [curr[0], curr[1] + 1]
        elif direction == "D":
            if -5 <= curr[1] - 1 <= 5:
                curr = [curr[0], curr[1] - 1]

        path.append(curr)
        path.sort()
        print(path)

        if path not in paths:
            paths.append(path)

    return len(paths)


print(solution("ULURRDLLU"))
