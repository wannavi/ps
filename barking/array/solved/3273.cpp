#include <iostream>
using namespace std;

int a[100005];
int dp[2000005];
int n, x;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int res = 0;
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> a[i];
  cin >> x;

  for (int i = 0; i < n; ++i) {
    if (x-a[i] > 0 && dp[x-a[i]]) res++;
    dp[a[i]] = 1;
  }

  cout << res;
}
