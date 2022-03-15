#include <iostream>
#include <string>
using namespace std;

int n;
int freq[26];

int main() {
  cin >> n;
  while (n--) {
    bool possible = true;
    string s1, s2;
    cin >> s1 >> s2;

    for (auto c : s1) freq[c-'a']++;
    for (auto c : s2) freq[c-'a']--;
    for (int i = 0; i < 26; ++i) 
      if (freq[i] != 0) possible = false;

    if (possible) cout << "Possible" << "\n";
    else cout << "Impossible" << "\n";

    fill(freq, freq+26, 0);
  }
}

