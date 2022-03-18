#include <bits/stdc++.h>
using namespace std;

int n, m;
int vis[69];

void dfs(vector<int> v) {
  if (size(v) == m) {
    for (auto &i : v) {
      printf("%d ", i);
      puts("");
      return
    }

    for (int i = 1; i <= n; i++) {
      if (!vis[i]) {
        vis[i] = 1;
        v.push_back(i);
        dfs(v);
        v.pop_back();
        vis[i] = 0;
      }
    }
  }

  int main() {
    cin >> n >> m;
    vector<int> a;
    dfs(a);
  }

