// Merge k Sorted Lists

/*
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
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
        if (a == NULL && b == NULL)
            return NULL;
        
        if (a == NULL)
            return b;
        
        if (b == NULL)
            return a;
        
        if (a->val > b->val){
            b->next = merge(a, b->next);
            return b;
        } else {
            a->next = merge(a->next, b);
            return a;
        }
    }
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) return NULL;
        
        if (lists.size() == 1) return lists.front();
        
        ListNode* res = lists[0];
        
        for (int i = 1; i < lists.size(); i++) {
            res = merge(res, lists[i]);
        }
        
        return res;
    }
};