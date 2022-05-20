#include <bits/stdc++.h>
using namespace std;
const int MAX = 101;
const int MOD = 1000000000;

long long dp[MAX][10];

int main() {
  int n; scanf("%d", &n);
  fill(dp[1] + 1, dp[1] + 10, 1);

  for (int i = 2; i <= n; ++i) {
    for (int j = 0; j < 10; ++j) {
      dp[i][j] += j == 0 ? 0 : dp[i - 1][j - 1] % MOD;
      dp[i][j] += j == 9 ? 0 : dp[i - 1][j + 1] % MOD;
    }
  }

  long long sum = 0;
  for (int i = 0; i < 10; ++i) 
    sum += dp[n][i] % MOD;

  printf("%lld\n", sum % MOD);
}

  
