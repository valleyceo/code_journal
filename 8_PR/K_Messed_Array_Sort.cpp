#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> sortKMessedArray( const vector<int>& arr, int k ) 
{
  // your code goes here
  // get +k more inputs
  priority_queue<int, vector<int>, greater<int> > pque;
  vector<int> res(arr.size(), 0);
  
  for (int i = 0; i < k; i++)
    pque.push(arr[i]);
  
  for (int i = 0; i < arr.size(); i++) {
    if (i+k < arr.size())
      pque.push(arr[i+k]);
    
    res[i] = pque.top();
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

Can you go to the settings (hover to the camera and see the setting button)
Have you checked the settings?

I will be back let me try different broswer OK No worries
- given array 
- each element is at most k places away from sorted position
- sorts arr

Input:
- arr

Output:
- sorted array

Req:
- time: 5000ms
- arr length = 100
- integer between 1~20

Time complexity: O(nlog(k)))
Space complexity: O(n + k) (O(k) if input array can be changed, current given is a const)
*/