// Sort List

/*
Sort a linked list in O(n log n) time using constant space complexity.
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
    ListNode* merge(ListNode* a, ListNode* b) {
        ListNode* l = new ListNode(0);
        ListNode* p = l;
        
        while (a != NULL && b != NULL){
            if (a->val > b->val){
                p->next = b;
                b = b->next;
            } else {
                p->next = a;
                a = a->next;
            }
            p = p->next;
        }
        
        if (a != NULL)
            p->next = a;
        
        if (b != NULL)
            p->next = b;
        
        return l->next;
    }
    
    ListNode* sortList(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
        
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        fast = slow->next;
        slow->next = NULL;
        
        return merge(sortList(head), sortList(fast));
    }
};