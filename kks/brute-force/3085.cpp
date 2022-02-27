#include <iostream>
#include <algorithm>
using namespace std;

int N;
char arr[50][50];

int getMaxCandies(int n) {
  int globalMax = 0;
  // horizontal
  for (int i = 0; i < n; ++i) {
    int localMax = 1, temp = 1;
    for (int j = 0; j < n - 1; ++j) {
      if (arr[i][j] == arr[i][j+1]) {
        temp++;
        localMax = max(localMax, temp);
      } else { 
        temp = 1;
      }
    }
    globalMax = max(globalMax, localMax);
  }
  // vertical
  for (int i = 0; i < n; ++i) {
    int localMax = 1, temp = 1;
    for (int j = 0; j < n - 1; ++j) {
      if (arr[j][i] == arr[j + 1][i]) {
        temp++;
        localMax = max(localMax, temp);
      } else { 
        temp = 1;
      }
    }
    globalMax = max(globalMax, localMax);
  }
  return globalMax;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;
  for (int i = 0; i < N; ++i) 
    for (int j = 0; j < N; ++j)
      cin >> arr[i][j];

  int res = getMaxCandies(N);
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N - 1; ++j) {
      // swap horizontal
      swap(arr[i][j], arr[i][j+1]);
      res = max(res, getMaxCandies(N));
      swap(arr[i][j], arr[i][j+1]);

      // swap vertical
      swap(arr[j][i], arr[j+1][i]);
      res = max(res, getMaxCandies(N));
      swap(arr[j][i], arr[j+1][i]);
    }
  }

  cout << res << '\n';
}
