#include <iostream>
#include <algorithm>
using namespace std;

int N, L;
int pos[1005];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> L;
  for (int i = 0; i < N; ++i) 
    cin >> pos[i];

  sort(pos, pos+N);

  int curr = 0, count = 1;
  for (int i = 1; i < N; ++i) {
    if (pos[i] - pos[curr] > L - 1) {
      count += 1;
      curr = i;
    }
  }

  cout << count << '\n';
}
    






