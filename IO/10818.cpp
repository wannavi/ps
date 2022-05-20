#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, tmp, min, max;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> tmp;
    if (i == 0) {
      min = max = tmp;
    }

    min = tmp < min ? tmp : min;
    max = tmp > max ? tmp : max;
  }

  cout << min << ' ' << max << '\n';
}

