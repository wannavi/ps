#include <bits/stdc++.h>
using namespace std;

int main() {
  // 1. memset
  // 0, -1 만 가능. 그리고 2차원 이상에서 문제발생.
  memset(a, 0, sizeof a);
  memset(b, 0, sizeof b);

  // 2. for
  for (int i = 0; i < 21; i++) 
    a[i] = 0;

  // 3. fill (*)
  fill(a, a+21, 0);
  for (int i = 0; i < 21; i++) 
    fill((b[i], b[i]+21, 0);

  // vector
  vector<int> v1(3, 5); // (5,5,5)
  cout << v1.size << '\n'; // 3
  v1.push_back(7);  // (5,5,5,7)

  vector<int> v2(2);  // (0, 0)
  v2.insert(v2.begin()+1, 3); // (0, 3, 0);

  vector<int> v3 = {1, 2, 3, 4};
  v3.erase(v3.begin()+2); // {1, 2, 4};

  vector<int> v4;
  v4 = v3;  // deep copy
  v4.pop_back();
  v4.clear();
}
