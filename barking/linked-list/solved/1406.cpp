#include <iostream>
#include <string>
#include <list>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  list<char> l;
  string s;
  int m; 
  cin >> s >> m;
  for (auto c : s) 
    l.push_back(c);

  auto it = l.end();
  while (m--) {
    char cmd, arg;
    cin >> cmd;

    if (cmd == 'L') {
      if (it != l.begin()) it--;
    } else if (cmd == 'D') {
      if (it != l.end()) it++;
    } else if (cmd == 'B') {
      if (it != l.begin()) {
        it = l.erase(--it);
      }
    } else if (cmd == 'P') {
      cin >> arg;
      l.insert(it, arg);
    }
  }

  for (auto c : l) cout << c;
}


