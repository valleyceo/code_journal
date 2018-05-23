#include <iostream>

using namespace std;

struct Node
{
   int key;
   Node *left;
   Node *right;
   Node *parent;
};

// Helper function that allocates a new Node 
Node* newNode( int key )
{
   Node* n = new Node;
   n->key = key;
   n->left = nullptr;
   n->right = nullptr;
   n->parent = nullptr;

   return n;
}

//  Given a binary search tree and a number, inserts a new Node with
//  the given number in the correct place in the tree. Returns the new
//  root pointer which the caller should then use 
Node *insert( Node *root, int key )
{
   // 1) If the tree is empty, return a new single Node
   if( root == nullptr )
      return newNode( key );

   Node *temp;

   // 2) Otherwise, recur down the tree
   if( key < root->key )
   {
      temp = insert( root->left, key );
      root->left = temp;
      temp->parent = root;
   } else
   {
      temp = insert( root->right, key );
      root->right = temp;
      temp->parent = root;
   }

   // Return the (unchanged) Node pointer
   return root;
}

// Return a pointer to a Node in the BST by its key.
// Use this fuction when you need a Node to test your 
// findInOrderSuccessor function on
Node *getNodeByKey( Node *root, int key )
{
   Node *currentNode = root;

   while( currentNode )
   {
      if( key == currentNode->key )
         return currentNode;

      if( key < currentNode->key )
         currentNode = currentNode->left;
      else
         currentNode = currentNode->right;
   }

   return nullptr;
}

Node* findInOrderSuccessor( Node *inputNode )
{
   // your code goes here
  // case 1
  if (inputNode->right) {
    inputNode = inputNode->right;
    
    while (inputNode->left) {
      inputNode = inputNode->left;
    }
    return inputNode;
  }
  
  // case 2
  while (inputNode->parent && inputNode->parent->left != inputNode)
    inputNode = inputNode->parent;
  
  if (inputNode->parent && inputNode->parent->left == inputNode)
    return inputNode->parent;
  else
    return NULL;
}

int main() {
  
  Node* root = newNode(20);
  //creating the tree given in the above diagram
  //root = insert(root, 20);
  root = insert(root, 9);
  root = insert(root, 25);
  root = insert(root, 5);
  root = insert(root, 12);
  root = insert(root, 11);  
  root = insert(root, 14);   
  
  // test cases
  Node* nine = root->left; // case 9 -> 11
  Node* fourteen = root->left->right->right; // 14 -> 20
  Node* eleven = root->left->right->left; // 11 -> 12
  Node* twentyfive = root->right; // 25 -> NULL
  
  Node* succ =  findInOrderSuccessor(twentyfive);
  cout << succ->key <<endl;
  return 0;
}

/*
Note:
- given Binary tree(inorder) and any node
- find the successor

case 1. 
if right child exist, then successor is always there

case 2.
if right child does not exist, traverse up until you find parent where you are left child

Time complexity (O(log(n)))
Space complexity (O(1))
*/