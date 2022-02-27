#include <iostream>
using namespace std;

int main() {
  int P, L, V;
  int count = 1;

  while (true) {
  cin >> L >> P >> V;
  if (L + P + V == 0) break;
  
  cout << "Case " << count << ": ";
  cout << ((int)V/P)*L + min(V%P, L) << '\n';
  count++;
  }
}
  
