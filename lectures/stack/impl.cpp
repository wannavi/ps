#include <iostream>
using namespace std;

const int MAX = 100005;
int data[MAX];
int pos = 0;

void push(int x) {
  data[pos++] = x;
}

void pop() {
  pos--;
}

int top() {
  return data[pos-1];
}

