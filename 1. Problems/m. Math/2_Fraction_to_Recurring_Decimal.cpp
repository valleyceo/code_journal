// Fraction to Recurring Decimal

/*
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
*/

// my solution
class Solution {
public:
    string fractionToDecimal(long long num, long long den) {
        if (num == 0) return "0";
        
        string res;
        
        if (num < 0 ^ den < 0) res += "-";
        
        num = abs(num);
        den = abs(den);
        
        res += to_string(num / den);
        
        if (num % den == 0) return res;
        
        res += '.';
        
        unordered_map<int, int> map;
        
        for (long long div = num % den; div; div %= den) {
            
            if (map.count(div) > 0) {
                res.insert(map[div], 1, '(');
                res += ')';
                break;
            }
            
            map[div] = res.size();
            
            div *= 10;
            
            res += to_string(div / den);
        }
        
        return res;
    }
};