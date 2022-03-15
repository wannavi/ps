## 코드 어떻게 짤지 고민을 해보고 정리해보자. (통일이 필요해!)

### Flood Fill는?

- BFS 를 사용해야한다.
  - 그렇다면 큐를 써야해!

```c++
#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int board[502][502] = {};
bool vis[502][502];
int n = 7, m = 10;

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main() {
  queue<pair<int,int>> Q;
  vis[0][0] = 1;
  Q.push({0,0});
  while (!Q.empty()) {
    pair<int,int> curr = Q.front(); Q.pop();
    cout << '(' << curr.X << ", " << curr.Y << endl;
    for (int dir = 0; dir < 4; dir++) {
      int nx = curr.X + dx[dir];
      int ny = curr.Y + dy[dir];
      if (nx < 0  || nx >= n || ny < 0 || ny >= m) continue;
      if (vis[nx][ny] || board[nx][ny] != 1) continue;
      vis[nx][ny] = 1;
      Q.push({nx,ny});
    }
  }
}
```

```python

```
