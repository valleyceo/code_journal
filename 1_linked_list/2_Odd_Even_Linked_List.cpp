// Odd Even Linked List

/*
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
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
    ListNode* oddEvenList(ListNode* head) {
        ListNode *ans = head;
        ListNode *odds = new ListNode(0);
        ListNode *evens = new ListNode(0);
        ListNode *odd_begin = odds;
        ListNode *even_begin = evens;
        int c = 1;
        
        while (ans) {
            if (c%2 == 1) {
                odds->next = new ListNode(ans->val);
                odds = odds->next;
            } else{
                evens->next = new ListNode(ans->val);
                evens = evens->next;
            }
            c++;
            ans = ans->next;
        }
        
        odds->next = even_begin->next;
        return odd_begin->next;
    }
};