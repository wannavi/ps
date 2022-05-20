#include <bits/stdc++.h>
using namespace std;

const int MAX = 1000005;
int dp[MAX];

int f(int n) {
  if (n == 1) return 0;
  if (dp[n] != -1) return dp[n];

  int res = f(n - 1) + 1;
  if (n % 3 == 0) res = min(res, f(n/3) + 1);
  if (n % 2 == 0) res = min(res, f(n/2) + 1);

  return dp[n] = res;
}

int main() {
  int n; scanf("%d", &n);
  fill(dp, dp + MAX, -1);

  printf("%d\n", f(n));
}
