#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, arr[100005];
  cin >> n;
  for (int i = 0; i < n; ++i)
    cin >> arr[i];

  int st, en, res = arr[0];
  while (st < n) {
    int tmp = 0;
    for (en = st; en < n; ++en) {
      tmp += arr[en];
      res = max(res, tmp);
      if (tmp + arr[en+1] < 0)
        break;
    }
    st = en + 1;
  }

  cout << res << '\n';
}

