n = int(input())
weights = []

for _ in range(n):
    weights.append(int(input()))

weights.sort()

# w1, w2, w3, ... , wn => w1 * n

result = 0
for i, weight in enumerate(weights):
    result = max(result, weight * (len(weights) - i))

print(result)
