// Array Index & Element Equality

/*
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[output] integer
*/

// my solution
#include <iostream>
#include <vector>

using namespace std;

int indexEqualsValueSearch(const vector<int> &arr) 
{
  // your code goes here
  int head, tail, mid;
  int lowest_ans = -1;
  head = 0;
  tail = arr.size();
  
  while (head < tail) {
    mid = head + (tail - head) / 2;
    if (arr[mid] == mid) {
      lowest_ans = mid;    
      tail = mid;
    } else if (arr[mid] < mid) {
      head = mid+1;
    } else {
      tail = mid;
    }
  }
  
  return lowest_ans;
}

int main() {
  return 0;
}

/* Note
- sorted array
- return lowest idx i for which arr[i] == i
- return -1 if not found
*/