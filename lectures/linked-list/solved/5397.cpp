#include <iostream>
#include <list>
#include <string>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int t; cin >> t;
  while (t--) {
    string s;
    cin >> s;

    list<char> l = {};
    auto it = l.end();
    for (char c : s) {
      if (c == '<') {
        if (it != l.begin()) it--;
      } else if (c == '>') {
        if (it != l.end()) it++;
      } else if (c == '-') {
        if (it != l.begin()) {
          it--;
          it = l.erase(it);
        }
      } else {
        l.insert(it, c);
      }
    }
    
    for (char c : l)
      cout << c;
    cout << '\n';
  }
}




