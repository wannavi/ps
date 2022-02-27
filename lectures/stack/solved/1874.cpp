#include <iostream>
#include <stack>
#include <string>
using namespace std;

stack<int> s;
string h;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n; cin >> n;

  int next = 1;
  while (n--) {
    int target; cin >> target;

    while (next <= target) {
      s.push(next++);
      h += "+\n";
    }
    if (s.top() != target) {
      cout << "NO\n";
      return 0;
    }
    s.pop();
    h += "-\n";
  }
  cout << h;
}
