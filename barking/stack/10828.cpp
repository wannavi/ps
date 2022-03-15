#include <iostream>
using namespace std;

class Stack {
private:
  int data[10005];
  int pos;

public:
  Stack(): pos(0) {}
  void push(int x) {
    data[pos++] = x;
  }
  int pop() {
    if (empty()) return -1;
    int res = top();
    pos--;
    return res;
  }
  int size() {
    return pos;
  }
  int empty() {
    return int(pos == 0);
  }
  int top() {
    if (empty()) return -1;
    return data[pos-1];
  }
};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  Stack s; 
  int n; cin >> n;
  while (n--) {
    string op;
    cin >> op;

    if (op == "push") {
      int t; cin >> t;
      s.push(t);
    } else if (op == "pop") {
      cout << s.pop() << '\n';
    } else if (op == "size") {
      cout << s.size() << '\n';
    } else if (op == "empty") {
      cout << s.empty() << '\n';
    } else if (op == "top") {
      cout << s.top() << '\n';
    }
  }
}
       
