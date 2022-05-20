#include <bits/stdc++.h>
using namespace std;

const int MAX = 11;
int dp[MAX];

int f(int n) {
  if (n == 1) return 1;
  if (n == 2) return 2;
  if (n == 3) return 4;
  if (dp[n]) return dp[n];

  dp[n] = f(n - 1) + f(n - 2) + f(n - 3);
  return dp[n];
}


int main() {
  int t, n; scanf("%d", &t);

  while (t--) {
    scanf("%d", &n);
    fill(dp, dp + MAX, 0);

    printf("%d\n", f(n));
  }
}

