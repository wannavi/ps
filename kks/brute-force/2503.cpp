#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool isPossible(string target, string num, int st, int ba) {
  // strike
  for (int i = 0; i < 3; ++i) 
    if (target[i] == num[i]) st--;

  // ball
  for (int i = 0; i < 3; ++i) { 
    for (int j = 0; j < 3; ++j) {
      if (i == j) continue;
      if (target[i] == num[j]) ba--;
    }
  }
  return st == 0 && ba == 0;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  vector<string> v;
  for (int i = 1; i < 10; ++i) {
    for (int j = 1; j < 10; ++j) { 
      for (int k = 1; k < 10; ++k) {
        if (i == j || i == k || j == k) 
          continue;
        v.push_back(to_string(100*i + 10*j + k));
      }
    }
  }

  string n;
  int t, st, ba; cin >> t;
  while (t--) {
    cin >> n >> st >> ba;
    for (auto it = v.begin(); it != v.end();) {
      if (!isPossible(*it, n, st, ba)) {
        it = v.erase(it);
      } else {
        ++it;
      }
    }
  }

  cout << v.size() << '\n';
}

