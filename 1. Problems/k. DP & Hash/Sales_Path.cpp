// Sales Path

/*
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

alt

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

Constraints:

[time limit] 5000ms

[input] Node rootNode

0 ≤ rootNode.cost ≤ 100000
[output] integer
*/

// my solution
#include <iostream>
#include <vector>

using namespace std;

struct Node
{
  int cost;
  vector<Node *> children;
  Node *parent;
};

int getCheapestCost( Node *rootNode )
{
  // your code goes here
  if (rootNode->children.size() == 0)
    return rootNode->cost;

  int min_cost = INT_MAX;

  for (auto node : rootNode->children) {
    min_cost = min(min_cost, getCheapestCost(node));
  }
  
  return min_cost + rootNode->cost;
}

int main() {
  Node* head = new Node();
  head->cost = 0;
  // lv1
  Node* lv11 = new Node();
  lv11->cost = 5;
  Node* lv12 = new Node();
  lv12->cost = 3;
  Node* lv13 = new Node();
  lv13->cost = 6;
  head->children.push_back(lv11);
  head->children.push_back(lv12);
  head->children.push_back(lv13);
  
  // lv2
  Node* lv21 = new Node();
  lv21->cost = 4;
  Node* lv22 = new Node();
  lv22->cost = 2;
  Node* lv23 = new Node();
  lv23->cost = 0;
  Node* lv24 = new Node();
  lv24->cost = 1;
  Node* lv25 = new Node();
  lv25->cost = 5;
  lv11->children.push_back(lv21);
  lv12->children.push_back(lv22);
  lv12->children.push_back(lv23);
  lv13->children.push_back(lv24);
  lv13->children.push_back(lv25);
  
  // lv3
  Node* lv31 = new Node();
  lv31->cost = 1;
  Node* lv32 = new Node();
  lv32->cost = 10;
  
  lv22->children.push_back(lv31);
  lv23->children.push_back(lv32);

  // lv4
  Node* lv41 = new Node();
  lv41->cost = 1;
  lv31->children.push_back(lv41);
  
  cout << getCheapestCost(head) << endl;
  return 0;
}

/* stack version
# p = root
s = []
dict = {}
sum = 0
while(s or p):
  if(p):
    s.put(<p, sum+p.cost>)
    if(len(p.child) == 0):
      p = None
    else:
      for i in range(0, len(p.child)):
        if (p.child[i] not in dict)
          p = p.child[i]
          dict[p.child[i]] = 1
          break
  if(p == None):
    <p, sumcost> = s.get()
    min_cost = min(min_cost, sumcost)
    for i in range(0, len(p.child)):
        if (p.child[i] not in dict)
          p = p.child[i]
          dict[p.child[i]] = 1
          break
          
  return min_cost
*/

/* Note:
- tree (not binary)
- root is the company
- ships to children nodes
- leaf node = car dealership
- cost of sales is the full path to the leaf

problem:
- get cheapest cost path

time complexity: O(N)

*/