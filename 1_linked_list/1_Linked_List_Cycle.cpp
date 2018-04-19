// Linked List Cycle

/*
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
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
    bool hasCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        ListNode* slow = new ListNode(0);
        ListNode* fast = new ListNode(0);
        slow = head;
        fast = head->next;
        
        while (fast->next != NULL && fast->next->next != NULL){
            fast = fast->next->next;
            slow = slow->next;
            
            if (fast->val == slow->val){
                return true;
            }
        }
        
        return false;
    }
};