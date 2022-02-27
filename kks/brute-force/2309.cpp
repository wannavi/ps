#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int arr[9], sum = 0;
  for (int i = 0; i < 9; ++i) {
    cin >> arr[i];
    sum += arr[i];
  }

  sort(arr, arr+9);

  int x1, x2;
  bool flag = false;
  for (x1 = 0; x1 < 9; ++x1) {
    for (x2 = x1 + 1; x2 < 9; ++x2) {
      if (x1 == x2) continue;
      if (arr[x1] + arr[x2] == sum - 100) {
        flag = true;
        break;
      }
    }
    if (flag) break;
  }

  for (int i = 0; i < 9; ++i)
    if (!(i == x1 || i == x2))
      cout << arr[i] << '\n';
}

