#include <bits/stdc++.h>
using namespace std;

const int MAX = 1005;
int dp[MAX];

int f(int n) {
  if (n == 1) return 1;
  if (n == 2) return 3;
  if (dp[n] != -1) return dp[n];

  dp[n] = (f(n - 1) + 2*f(n - 2)) % 10007;
  return dp[n];
}

int main() {
  int n; cin >> n;
  fill(dp, dp + MAX, -1);

  printf("%d\n", f(n));
}
