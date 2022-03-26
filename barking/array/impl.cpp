#include <iostream>
using namespace std;

void insert(int pos, int num, int arr[], int& len) {
  for (int i = len; i > pos; i--) 
    arr[i] = arr[i - 1];
  arr[pos] = num;
  len++;
}

void erase(int pos, int arr[], int& len) {
  for (int i = pos; i < len - 1; i++) 
    arr[i] = arr[i + 1];
  len--;
}

void printArr(int arr[], int len) {
  for (int i = 0; i < len; i++)
    cout << arr[i] << ' ';
  cout << '\n';
}

int main(void) {
  int arr[10] = {10, 50, 40, 30, 70, 20};
  int len = 6;

  insert(3, 60, arr, len);
  printArr(arr, len);

  erase(4, arr, len);
  printArr(arr, len);
}
