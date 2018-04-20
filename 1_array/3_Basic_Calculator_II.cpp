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

// my solution 1. - recursive, no solution
class Solution {
public:
    int calculate(string s) {
        double res = recurse(s);
        return res;
    }
    
private:
    int recurse(string s) {
        // number if length is below 2
        if (s.length() < 3) {
            return stod(s);
        }
        
        // add and minus
        for (int i = s.length()-1; i >= 0; i--) {
            if (s[i] == '+') {
                //cout << "plus: " << recurse(s.substr(0, i)) + recurse(s.substr(i+1)) << endl;
                return recurse(s.substr(0, i)) + recurse(s.substr(i+1));
            } else if (s[i] == '-') {
                return recurse(s.substr(0, i)) - recurse(s.substr(i+1));
            }
        }
        
        // multiply and divide
        for (int i = s.length()-1; i >= 0; i--) {
            if (s[i] == '*') {
                return recurse(s.substr(0, i)) * recurse(s.substr(i+1));
            } else if (s[i] == '/') {
                return recurse(s.substr(0, i)) / recurse(s.substr(i+1));
            }
        }
        cout << s << endl;
        return stod(s);
    }
};