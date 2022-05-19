#include <bits/stdc++.h>
using namespace std;

const int days_in_month[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const string week[] = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};

int md_to_days(int m, int d) {
  int res = d;
  for (int i = 1; i < m; ++i) 
    res += days_in_month[i];

  return res;
}

int main() {
  int m, d, diff;
  cin >> m >> d;

  diff = md_to_days(m, d) - 1;
  cout << week[diff % 7] << '\n';
}





