#include <iostream>
#include <list>
using namespace std;

int N, K;

int main() {
  cin >> N >> K;

  list<int> L = {};
  for (int i = 1; i <= N; ++i)
    L.push_back(i);

  auto it = L.begin();
  cout << "<";
  while (true) {
    for (int i = 0; i < K-1; ++i) {
      it++;
      if (it == L.end()) 
        it = L.begin();
    }
    cout << *it;
    it = L.erase(it);
    if (it == L.end())
      it = L.begin();

    if (L.begin() != L.end())
      cout << ", ";
    else 
      break;
  }
  cout << ">";
}

