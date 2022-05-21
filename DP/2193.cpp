#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAX = 100;

// [LENGTH][END_NUMBER]
ll dp[MAX][2];

int main() {
  int n; scanf("%d", &n);
  for (int i = 0; i < MAX; ++i)
    fill(dp[i], dp[i] + 2, 0);

  dp[1][1] = 1;

  for (int i = 2; i <= n; ++i) {
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
    dp[i][1] = dp[i - 1][0];
  }

  printf("%lld\n", dp[n][0] + dp[n][1]);
}


