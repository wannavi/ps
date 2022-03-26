#include <iostream>
using namespace std;

const int MAX = 1000005;
int data[MAX], prev[MAX], next[MAX];
int unused = 1;

void insert(int addr, int num) {
  prev[unused] = addr;
  data[unused] = num;
  next[unused] = addr;

  if (next[addr] != -1) 
    prev[next[addr]] = unused;

  prev[addr] = unused;
  unsed++;
}

void erase(int addr) {
  next[prev[addr]] = next[addr];
  if (next[addr] != -1)
    prev[next[addr]] = prev[addr];
}

void traverse() {
  int cur = next[0];
  while (cur != -1) {
    cout << data[cur] << ' ';
    cur = next[cur];
  }
  cout << '\n';
}

int main() {
  fill(prev, prev+MAX, -1);
  fill(next, next+MAX, -1);
}
