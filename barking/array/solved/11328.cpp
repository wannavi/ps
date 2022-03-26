#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n;
int freq[26];

int main() {
  cin >> n;

  while (n--) {
    string s1, s2;
    cin >> s1 >> s2;

    // O(NlogN)
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    if (s1 == s2) cout << "Possible" << '\n';
    else cout << "Impossible" << '\n';
  }
}
