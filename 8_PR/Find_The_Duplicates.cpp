// Find The Duplicates

/*
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2
Constraints:

[time limit] 5000ms

[input] array.integer arr1

1 ≤ arr1.length ≤ 100
[input] array.integer arr2

1 ≤ arr2.length ≤ 100
[output] array.integer
*/

// my solution
#include <iostream>
#include <vector>

using namespace std;

int binary_search(vector<int>& arr1, int find, int min_idx) {
  int low = min_idx;
  int high = arr1.size()-1;
  
  while (low < high) {
    int mid = low - (high - low) / 2;
    
    if (find == arr1[mid]) {
      return find;
    }else if (find < arr1[mid]) {
      high = mid;
    } else {
      low = mid+1;
    }
  }
}
//(N)Log(M) - (Log M)
// [1,4,6,7,9,10]

vector<int> findDuplicates( const vector<int>& arr1, const vector<int>& arr2) 
{
  // your code goes here
  vector<int> res;
  int n = arr1.size();
  int m = arr2.size(); // longer
  
  int idx1 = 0, idx2 = 0;
  
  while(idx1 < n && idx2 < m) {
    
    if (arr1[idx1] == arr2[idx2]) {
      res.push_back(arr1[idx1]);
      idx1++;
      idx2++;
    } else if (arr1[idx1] < arr2[idx2]) {
      idx1++;
    } else {
      idx2++;
    }
  }
  
  return res;
}

int main() {
  return 0;
}

/*
Note:
- two arrays arr1, arr2 (sorted)
- return an array of all numbers that are both in arr1, arr2
- output should be sorted

Limit
arr1, arr2: 1~100

Case:
arr1 =  [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]

output:
out = [3,6]

time complexity: O(n)
space complexity: O(1)

Case2:
arr1 = [1, 500]
arr2 = [1, 3, 5, 6, 7, 8, 9, 10... ~1000]

O(log(n2)*n1)
*/