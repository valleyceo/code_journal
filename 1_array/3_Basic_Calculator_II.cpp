// Basic Calculator II

/*
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
*/

// my solution (19ms, best->12ms)
class Solution {
public:
    int calculate(string s) {
        string num = "";
        stack<char> sign;
        stack<int> nums;
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                num += s[i];
            } else if (s[i] == ' ') {
                continue;
            } else { // +,-,*,/
                // push in new number
                int new_num = stoi(num);
                nums.push(new_num);
                num = "";
                
                // +, - -> should reduce all signs and have 1 ans
                if (s[i] == '+' || s[i] == '-') {
                    while (!sign.empty()) {
                        int num1 = nums.top();
                        nums.pop();
                        nums.top() = compute(nums.top(), num1, sign.top());
                        sign.pop();
                    }
                // *, / -> should reduce the last signs only if it's *,/
                } else {
                    if (!sign.empty() && (sign.top() == '*' || sign.top() == '/')) {
                        int num1 = nums.top();
                        nums.pop();
                        nums.top() = compute(nums.top(), num1, sign.top());
                        sign.pop();
                    }
                }
                
                sign.push(s[i]);
            }
        }
        
        // push in last number
        int new_num = stoi(num);
        nums.push(new_num);
        
        // check if there is any sign left
        while (!sign.empty()) {
            int num1 = nums.top();
            nums.pop();
            nums.top() = compute(nums.top(), num1, sign.top());
            sign.pop();
        }
        
        return nums.top();
    }
    
private:
    int compute(int a, int b, char sign) {
        if (sign == '+') {
            return a + b;
        } else if (sign == '-') {
            return a - b;
        } else if (sign == '*') {
            return a * b;
        } else if (sign == '/') {
            return a / b;
        }
    }
};