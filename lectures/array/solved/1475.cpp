// 방 번호
#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int N, res;
  cin >> N;

  int freq[10] = {};
  while (N) {
    freq[N%10]++;
    N /= 10;
  }

  for (int i = 0; i < 10; i++) { 
    if (i == 6 || i == 9) continue;
    res = max(res, freq[i]);
  }

  ans = max(ans, (a[6]+a[9]+1)/2);
  cout << max;
}

  

