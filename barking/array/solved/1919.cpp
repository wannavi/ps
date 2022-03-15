#include <iostream>
#include <string>
using namespace std;

int freq[26];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  string s1, s2;
  cin >> s1 >> s2;

  for (char c : s1) freq[c-'a']++;
  for (char c : s2) freq[c-'a']--;

  int res = 0;
  for (int i = 0; i < 26; ++i) 
    res += freq[i] > 0 ? freq[i] : -freq[i];

  cout << res;
}

