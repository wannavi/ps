#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  vector<int> vec;
  for (int i = 1; i*(i+1)/2 <= 1000; ++i)
    vec.push_back(i*(i+1)/2);

  int t;
  cin >> t;

  while (t--) {
    int u;
    cin >> u;
    int ok = 0;
    for (int i = 0; i < vec.size(); ++i) 
      for (int j = 0; j <= i; ++j)
        for (int k = 0; k <= j; ++k)
          if (vec[i] + vec[j] + vec[k] == u)
            ok = 1;

    cout << ok << '\n';
  }
}


