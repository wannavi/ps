#include <bits/stdc++.h>
using namespace std;

int dp[1000005] = {0,0,1,};

int main() {
  int n; scanf("%d", &n);

  for (int i = 3; i <= n; ++i) {
    dp[i] = dp[i-1] + 1;

    if (i % 3 == 0) 
      dp[i] = dp[i] < dp[i/3] + 1 ? dp[i] : dp[i/3] + 1;

    if (i % 2 == 0) 
      dp[i] = dp[i] < dp[i/2] + 1 ? dp[i] : dp[i/2] + 1;
  }

  cout << dp[n] << '\n';
}

