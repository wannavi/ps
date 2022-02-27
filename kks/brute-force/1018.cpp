#include <iostream>
using namespace std;

int n, m;
char arr[50][50];

int getBlockWillPaint(int x, int y) {
  int res = 0;
  // assume that first block is white
  bool isWhite = true;
  for (int i = x; i < x + 8; ++i) {
    for (int j = y; j < y + 8; ++j) {
      if (isWhite && arr[i][j] == 'B') res++;
      if (!isWhite && arr[i][j] == 'W') res++;
      isWhite = !isWhite;
    }
    isWhite = !isWhite;
  }
  return min(res, 64 - res);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> m >> n;
  for (int i = 0; i < m; ++i)
    for (int j = 0; j < n; ++j)
      cin >> arr[i][j];

  int res = getBlockWillPaint(0, 0);
  for (int i = 0; i <= m - 8; ++i) 
    for (int j = 0; j <= n - 8; ++j)
      res = min(res, getBlockWillPaint(i, j));

  cout << res << '\n';
}
