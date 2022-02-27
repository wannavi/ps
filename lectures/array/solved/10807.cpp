#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, v, t;
  vector<int> vec;

  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> t;
    vec.push_back(t);
  }
  cin >> v;

  int cnt = 0;
  for (auto p : vec) 
    if (p == v) cnt++;

  cout << cnt;
}
