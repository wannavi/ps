#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, i, j; cin >> n;

  for (i = 0; i < n; ++i) {
    for (j = 0; j < n - i - 1; ++j)
      cout << ' ';

    for (j = 0; j < 2*i + 1; ++j) {
      if (0 < i && i < n - 1) {
        if (j == 0 || j == 2*i) {
          cout << '*';
        } else {
          cout << ' ';
        }
      } else {
        cout << '*';
      }
    }
    cout << '\n';
  }
}


