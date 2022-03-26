"""
- 동전의 액수가 서로 배수 관계가 아니면 그리디한 방법으로 풀 수 없다.
- n번째 동전부터만 사용할 때, k원을 나타내는 최소 동전 개수

f(n,k) = 
    1 (n=N, k=0)
    0 (n=N, k>0)
    min(f(n+1, k-cost[n]*i)+i) (k >= cost[n]*i 인 모든 0 이상인 정수 i)
"""
import sys

sys.setrecursionlimit(1000000)

IMPOSSIBLE = sys.maxsize
N, K = map(int, input().split())
cost = [int(input()) for _ in range(N)]
dp = [[-1] * (K + 1) for _ in range(N + 1)]


def F(n: int, k: int) -> int:
    if n == N:
        return 0 if k == 0 else IMPOSSIBLE

    result = F(n + 1, k)
    if k >= cost[n]:
        result = min(result, F(n, k - cost[n] + 1))

    dp[n][k] = result
    return result


result = F(0, K)
if result == IMPOSSIBLE:
    print("-1")
else:
    print(result)
