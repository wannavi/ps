#include <iostream>
using namespace std;

int freq[10];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int A, B, C, r;
  cin >> A >> B >> C;
  int prod = A*B*C;

  while (prod) {
    freq[prod % 10]++;
    prod /= 10;
  }

  for (int i = 0; i < 10; i++)
    cout << freq[i] << '\n';
}

