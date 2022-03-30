# 수들의 합 2

N, M = map(int, input().split())
A = list(map(int, input().split()))

lo, hi = 0, 0
acc, count = 0, 0

""" [lo, hi)
1. acc < M: hi를 하나 증가시켜본다. 
2. acc = M: count를 늘리고lo를 하나 증가시켜본다.
3. acc > M: lo를 하나 증가시켜본다.
"""
while lo < N:
    if acc < M:
        if hi == N:
            break

        acc += A[hi]
        hi += 1
    else:
        if acc == M:
            count += 1
        acc -= A[lo]
        lo += 1

print(count)
