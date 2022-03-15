#include <list>
using namespace std;

int main() {
  list<int> l = {1, 2};
  list<int>::iterator it = l.begin();
  
  cout << *it << '\n';
  l.push_back(5);
  l.insert(it, 6);

  it++;
  it = l.erase(it);

  cout << *it << '\n';

  for (auto v : l) 
    cout << v << ' ';

  for (auto iter = l.begin(); iter != l.end(); iter++)
    cout << *iter << ' ';
}



