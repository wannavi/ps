n = int(input())
tasks = []

for _ in range(n):
    tasks.append(tuple(map(int, input().split())))

tasks.sort(key=lambda v: (v[1], v[0]))

end = count = 0
for task in tasks:
    if end <= task[0]:
        continue

    end = task[1]
    count += 1

print(count)
