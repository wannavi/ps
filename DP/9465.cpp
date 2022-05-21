#include <bits/stdc++.h>
using namespace std;
const int MAX = 100005;

int scores[2][MAX];
int dp[MAX][3];

int main() {
  int t, n; scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);

    for (int i = 0; i < 2; ++i) 
      for (int j = 0; j < n; ++j)
        scanf("%d", &scores[i][j]);

    dp[0][1] = scores[0][0], dp[0][2] = scores[1][0];
    for (int i = 0; i < n - 1; ++i) {
      dp[i+1][0] = max(dp[i][0], max(dp[i][1], dp[i][2]));
      dp[i+1][1] = max(dp[i][0], dp[i][2]) + scores[0][i+1];
      dp[i+1][2] = max(dp[i][0], dp[i][1]) + scores[1][i+1];
    }

    printf("%d\n", max(dp[n-1][0], max(dp[n-1][1], dp[n-1][2])));
  }
}

