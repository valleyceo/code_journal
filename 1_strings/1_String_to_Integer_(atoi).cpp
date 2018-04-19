// String to Integer (atoi)

/*
mplement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
*/

// my solution
class Solution {
public:
    int myAtoi(string str) {
        if(((str[0]-'0'<0)||(str[0]-'9'>0))&&(str[0]!='+')&&(str[0]!='-')&&(str[0]!=' ')){
            return 0;
        }
        
        double d, prev_n = 0, n = 0;
        double start = 0;
        bool neg = false;
        
        while(str[start]==' ')
        {
            start++;
        }
        
        if (str[start] == '-'){
            start += 1;
            neg = true;
        }else if (str[start] == '+'){
            start += 1;
        }
        
        for (int i=start; i<str.length(); i++) {
            if ((str[i]>='0')&&(str[i]<='9')){
                d = str[i] - '0';
                n = (n*10) + d;
                
            } else {
                break;
            }
        }
        
        n = neg ? -n : n;
        if (n > 2147483647){
            return 2147483647;
        } else if (n < -2147483648){
            return -2147483648;
        } else {
            return n;
        }
        
    }
};