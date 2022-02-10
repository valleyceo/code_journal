// Palindrome Linked List

/*
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
*/

// my solution - O(n), need to improve
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
    bool isPalindrome(ListNode* head) {
        vector<int> arr;
        
        while(head) {
            arr.push_back(head->val);
            head = head->next;
        }
        
        for (int i=0; i<arr.size()/2; i++) {
            if (arr[i] != arr[arr.size()-1-i]){
                return false;
            }
        }
        return true;
    }
};