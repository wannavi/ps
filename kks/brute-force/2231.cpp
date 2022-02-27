#include <iostream>
#include <algorithm>
using namespace std;

int de(int n) {
  int sum = n;
  while (n) {
    sum += n % 10;
    n /= 10;
  }
  return sum;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int N; // sum of decomp(M) => N
  cin >> N;

  for (int M = 0; M < N; ++M) {
    if (de(M) == N) {
      cout << M << '\n';
      return 0;
    }
  }

  cout << 0 << '\n';
}

