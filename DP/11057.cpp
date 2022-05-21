#include <bits/stdc++.h>
using namespace std;
const int MAX = 1005;
const int MOD = 10007;

// (LENGTH, END_NUMBER)
int dp[MAX][10];

int main() {
  int n; scanf("%d", &n);
  fill(dp[1], dp[1] + 10, 1);

  for (int i = 2; i <= n; ++i) {
    for (int j = 0; j < 10; ++j) {
      for (int k = 0; k <= j; ++k) {
        dp[i][j] += dp[i-1][k];
      }
      dp[i][j] %= MOD;
    }
  }

  int sum = 0;
  for (int i = 0; i < 10; ++i)
    sum += dp[n][i] % MOD;

  printf("%d\n", sum % MOD);
}



