#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> sortKMessedArray( const vector<int>& arr, int k ) 
{
  // your code goes here
  // get +k more inputs
  priority_queue<int, vector<int>, greater<int> > pque;
  vector<int> res;
  
  for (int i = 0; i <= k; i++) {
    pque.push(arr[i]);
  }
  
  for (int i = k + 1; i < arr.size(); i++) {
    res.push_back(pque.top());
    pque.pop();
    
    pque.push(arr[i]);
  }
  
  while (!pque.empty()) {
    res.push_back(pque.top());
    pque.pop();
  }
  
  return res;
}

int main() {
  
  vector<int> A = {1, 4, 5, 2, 3, 7, 8, 6, 10, 9};
  int k = 2;
  vector<int> res;
  res = sortKMessedArray(A, k);
  
  for (int &i : res) {
    cout << i << " ";
  }
  
  return 0;
}


/* note:
- given array 
- each element is at most k places away from sorted position
- sorts arr

Input:
- arr

Output:
- sorted array

Limit:
- time: 5000ms
- arr length = 100
- integer between 1~20

Time complexity: O(n) -> assume small K O(log(k)) ~ O(1)
Space complexity: O(n)
*/