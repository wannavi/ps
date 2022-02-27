#include <iostream>
#include <string>
using namespace std;

int main() {
  string s; 
  cin >> s;

  int count[26] = {0,};
  for (char c: s) 
    count[c - 'a'] += 1;

  for (int i = 0; i < 26; i++)
    cout << count[i] << ' ';
}


