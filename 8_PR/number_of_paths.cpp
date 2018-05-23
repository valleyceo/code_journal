#include <iostream>
#include <vector>
using namespace std;

unsigned long long int numOfPathsToDest( int n ) 
{
  if (n == 1)
    return 1;
  
  // your code goes here
  vector<unsigned long long int > arr(n, 0);
  arr[0] = 1;
  
  for (int i = 1; i < n; i++) {
    for (int j = 1; j < n; j++) {
      if (i == j) {
        arr[j] = arr[j - 1];
        break;
      }
      arr[j] += arr[j-1];
    }
  }
  
  return arr[n-1];
}

int main() {
  //cout << numOfPathsToDest(100) << endl;
  return 0;
}

/* Note:
Number of paths
- nxn grid
- move to diagonally opposite location
- Can only move top, right, cannot pass red line

Input:
- n (nxn)

output:
- x: maximum different routes

Limit:
- time: 5000ms
- n: 1 ~ 100

n = 2
   .1
.1 .1
-> 1

n = 3
      .1
   .1 .1
.2 .2 .1
-> 2
n = 4
         .1
      .1 .1
   .2 .2 .1
.5 .5 .3 .1

Complexity:
- time complexity: O(n(n-1)/2) ~ O(n^2)
- space complexity: O(n)
*/