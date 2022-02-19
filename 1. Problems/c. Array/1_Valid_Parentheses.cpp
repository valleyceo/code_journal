// Valid Parentheses

/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
*/

// my solution
class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        
        for (char a: s) {
            if (a == '(' || a == '{' || a == '['){
                stk.push(a);
                continue;
            } else if (a == ')' || a == '}' || a == ']'){
                if (stk.empty())
                    return false;
            
                if (a == ')'){
                    if (stk.top() == '(') {
                        stk.pop();
                    } else {
                        return false;
                    }
                } else if (a == '}'){
                    if (stk.top() == '{') {
                        stk.pop();
                    } else {
                        return false;
                    }
                } else if (a == ']'){
                    if (stk.top() == '[') {
                        stk.pop();
                    } else {
                        return false;
                    }
                }
            }
            
            
        }
        return stk.empty() ? true : false;
    }
};