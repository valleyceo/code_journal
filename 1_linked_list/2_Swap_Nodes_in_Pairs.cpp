// Swap Nodes in Pairs

/*
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        
        ListNode* ans = head->next;
        ListNode* one = head;
        ListNode* two = head->next;
        
        while (two->next != NULL && two->next->next != NULL) {
            ListNode* three = two->next;
            ListNode* four = two->next->next;
            one->next = four;
            two->next = one;
            one = three;
            two = four;
        }
        
        if (two->next == NULL) {
            two->next = one;
            one->next = NULL;
        } else {
            one->next = two->next;
            two->next = one;
        }
        
        return ans;
    }
};