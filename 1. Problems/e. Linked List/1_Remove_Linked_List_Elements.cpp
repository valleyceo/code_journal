// Remove Linked List Elements

/*
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
*/

// my solution
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        // remove front
        while (head && head->val == val)
            head = head->next;
        
        if (!head) return NULL;
        
        ListNode* node = head;
        
        // remove middle
        while (node->next != NULL && node->next->next != NULL) {
            if (node->next->val == val)
                node->next = node->next->next;
            else
                node = node->next;
        }
        
        // remove tail
        if (node->next != NULL && node->next->val == val)
            node->next = NULL;
        
        return head;
    }
};

// alternative
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (!head) return NULL;
        
        ListNode* new_head = new ListNode(0);
        new_head->next = head;
        ListNode* node = new_head;
        
        while (node) {
        	while (node->next && node->next->val == val)
        		node->next = node->next->next;

        	node = node->next;
        }

        return new_head->next;
    }
};