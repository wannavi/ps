#include <iostream>
using namespace std;

int N, K;
int a[6][2] = {};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> K;

  for (int i = 0; i < N; ++i) {
    int a, b;
    cin >> a >> b;
    a[Y-1][S]++;
  }

  int ans = 0;
  for (int i = 0; i < 6; ++i) {
    for (int j = 0; j < 2; ++j) {
      ans += a[i][j]/K;
      if (a[i][j]%K) ans++;
    }
  }
  cout << ans;
}
