#include <iostream>
#include <vector>
using namespace std;

int arr[500005];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n; cin >> n;
  arr[0] = 100000005;
  for (int i = 1; i <= n; ++i)
    cin >> arr[i];

  // 처음으로 나보다 큰 왼쪽 기둥
  for (int r = 1; r <= n; r++) {
    for (int l = r - 1; l >= 0; l--) {
      if (arr[l] >= arr[r]) {
        cout << l << ' ';
        break;
      }
    }
  }
}

