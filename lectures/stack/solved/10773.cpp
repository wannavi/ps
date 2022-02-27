#include <iostream>
#include <stack>
using namespace std;

stack<int> s;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n; cin >> n;
  while (n--) {
    int t; cin >> t;
    if (t == 0) s.pop();
    else s.push(t);
  }

  int r = 0;
  while (!s.empty()) {
    r += s.top();
    s.pop();
  }

  cout << r << '\n';
}




