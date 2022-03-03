class Solution:
    def __init__(self):
        self.dp = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]

        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]

    def fib_bottomup(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[n]
