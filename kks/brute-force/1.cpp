#include <cstdio>
#include <algorithm>
using namespace std;

// O(N^2)

int main() {
  int N, arr[1000];
  scanf("%d", &N);

  for (int i = 0; i < N; ++i)
    scanf("%d", arr+i);

  int res = 0;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      if (i != j) 
        res = max(res, arr[i] + arr[j]);

  printf("%d\n", res);
}
