// Insert into a Cyclic Sorted List

/*
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.

In the figure above, there is a cyclic sorted list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list.

The new node should insert between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
*/

// my solution
/*
// Definition for a Node.
class Node {
public:
    int val = NULL;
    Node* next = NULL;

    Node() {}

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        if (head == NULL) {
            Node* new_head = new Node(insertVal, NULL);
            new_head->next = new_head;
            return new_head;
        }
        
        Node* node = head;
        
        while (1) {
            if (node->val == node->next->val)
                break;
            
            if (node->val <= insertVal && insertVal <= node->next->val)
                break;
            
            if (node->val > node->next->val) {
                if (insertVal >= node->val || insertVal <= node->next->val)
                    break;
            }
            
            node = node->next;
        }
        
        node->next = new Node(insertVal, node->next);
        
        return head;
    }
};

/* Note
3->6->9->3
pev > new > next
could be in middle: 5

prev < new && prev > next
could be the biggest: 12

new < next && prev > next
could be the smallest: 1

*/