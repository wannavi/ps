n, target = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
count = 0

for coin in coins:
    q, r = divmod(target, coin)

    if q:
        target = r
        count += q

print(count)
