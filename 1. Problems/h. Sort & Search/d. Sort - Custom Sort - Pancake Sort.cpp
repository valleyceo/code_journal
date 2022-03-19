// Pancake Sort

/*
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

Constraints:

[time limit] 5000ms

[input] array.integer arr

[input] integer k

0 ≤ k
[output] array.integer
*/

// my solution
#include <iostream>
#include <vector>

using namespace std;

void flip(vector<int>& arr, int k) {
  for (int i = 0; i < k/2; i++) {
    int temp = arr[i];
    arr[i] = arr[k-1-i];
    arr[k-1-i] = temp;
  }
}

vector<int> pancakeSort( const vector<int>& arr ) 
{
  // your code goes here
  // find largest element
  vector<int> res(arr);
  
  if (arr.size() < 2)
    return res;
  
  int max_val, max_ind;
  for (int i = res.size()-1; i >= 0; i--) {
    max_val = -1;
    
    for (int j = 0; j <= i; j++) {
      if (max_val < res[j]) {
        max_val = res[j];
        max_ind = j;
      }
    }
    
    if (max_ind == i)
      continue;
    
    if (max_ind != 0)
      flip(res, max_ind + 1);
    
    flip(res, i + 1);
  }
  
  return res;
}

int main() {
  return 0;
}


/* Note
- flip: reverse first k elements in arr
- pancakesort: sorts and returns the input array


arr = 3 1 2
      2 1 3
      1 2 3
      
      
arr = 3 4 1 2
      4 3 1 2
      2 1 3 4
      1 2 3 4

flip complexity: O(N)
Time complexity: O(find the largest + flip) = O(2N * N) = O(N^2)
Space complexity: O(1) -inplace
*/