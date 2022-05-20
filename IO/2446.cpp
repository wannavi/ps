#include <bits/stdc++.h>
using namespace std;

int main() {
  int n; cin >> n;

  /* n - 1 */
  for (int i = 0; i < n - 1; ++i) {
    for (int j = 0; j < i; ++j)
      cout << ' ';

    for (int j = 0; j < 2*(n - i) - 1; ++j)
      cout << '*';

    cout << '\n';
  }

  /* n */
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n - i - 1; ++j)
      cout << ' ';

    for (int j = 0; j  < 2*i + 1; ++j) 
      cout << '*';

    cout << '\n';
  }
}

