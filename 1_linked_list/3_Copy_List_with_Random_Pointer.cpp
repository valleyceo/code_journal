// Copy List with Random Pointer

/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
*/

// my solution
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */

// https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43507/Easy-to-understand-C++

class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (head == NULL) return NULL;
        
        RandomListNode* orig = head, *copy = NULL;
        
        // insert copy between every node
        while (orig) {
            copy = new RandomListNode(orig->label);
            copy->next = orig->next;
            orig->next = copy;
            
            // skip over new copy and iterate
            orig = orig->next->next;
        }
        
        orig = head;
        
        // update random pointers on copy
        while (orig) {
            copy = orig->next;
            
            if (orig->random) {
                copy->random = orig->random->next;
            }
            
            orig = orig->next->next;
        }
        
        orig = head;
        RandomListNode* copyHead = head->next;
        copy = copyHead;
        
        // separate the orig / copy list
        while (copy && copy->next) {
            orig->next = orig->next->next; // combine odd
            copy->next = copy->next->next; // combine even
            
            //iterate forward
            orig = orig->next;
            copy = copy->next;
        }
        
        // remove the last copied node from original list
        orig->next = NULL;
        
        return copyHead;
    }
};