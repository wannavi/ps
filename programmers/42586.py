def solution(progress, speeds):
    res = []
    time = 0

    while progress:
        count = 0
        while progress and progress[0] + time * speeds[0] >= 100:
            progress.pop(0)
            speeds.pop(0)
            count += 1

        time += 1
        if count:
            res.append(count)

    return res
