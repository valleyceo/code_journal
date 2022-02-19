// Merging 2 Packages

/*
Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input] integer limit

[output] array.integer
*/

// my solution
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> getIndicesOfItemWeights( const vector<int>& arr, int limit)
{
  // your code goes here
  /*
  limit = 21
    arr.at(i);
    arr = [4, 6, 10, 15, 16]
                      ^
    umap = {[4, 0], [6, 1], [10, 2], found ->return[3, 1]}
    
    time complexity: O(n)
    space complexity: O(n)

  */
  unordered_map<int, int> umap; // [value, idx]
  vector<int> res;
  
  for (int i = 0; i < arr.size(); i++) {
    if (umap.find(limit - arr[i]) == umap.end()) {
      umap[arr[i]] = i;
    } else {
      res.push_back(i);
      res.push_back(umap[limit - arr[i]]);
      return res;
    }
  }
  
  return res;
}


int main() {
  return 0;
}