n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0
for p, q in zip(a, b):
    result += p * q

print(result)
