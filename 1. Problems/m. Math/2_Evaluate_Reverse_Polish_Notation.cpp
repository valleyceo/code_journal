// Evaluate Reverse Polish Notation

/*
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
*/

// my solution
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        int a, b;
        
        for (string n : tokens) {
            if (n == "+") {
                a = stk.top();
                stk.pop();
                b = stk.top();
                stk.pop();
                stk.push(b+a);
            } else if (n == "-") {
                a = stk.top();
                stk.pop();
                b = stk.top();
                stk.pop();
                stk.push(b-a);
            } else if (n == "*") {
                a = stk.top();
                stk.pop();
                b = stk.top();
                stk.pop();
                stk.push(b*a);
            } else if (n == "/") {
                a = stk.top();
                stk.pop();
                b = stk.top();
                stk.pop();
                stk.push(b/a);
            } else {
                stk.push(stoi(n));
            }
        }
        
        return stk.top();
    }
};