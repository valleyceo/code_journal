// Largest Palindrome Product

/*
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
*/

// my solution - Exceeds time limit at n=7
class Solution {
public:
    bool is_palindrome(long long int n) {
        string num = to_string(n);
        for (int i = 0; i <= num.length()/2; i++) {
            if (num[i] != num[num.length() - i - 1])
                return false;
        }
        
        return true;
    }
    int largestPalindrome(int n) {
        long long int top = pow(10, n) - 1;
        long long int bot = pow(10, n-1);
        long long int res = 0;
        long long int prod;
        
        for (long long int i = top; i >= bot; i--) {
            for (long long int j = top; j >= bot; j--) {
                prod = i * j;
                
                if (prod <= res)
                    break;
                
                if (is_palindrome(prod)) {
                    if (prod > res)
                        res = prod;
                }
            }
        }
        return res % 1337;
    }
};

// solution
// https://leetcode.com/problems/largest-palindrome-product/discuss/96325/C++-From-product-to-palindrome

class Solution {
public:
    int largestPalindrome(int n) {
        long max, min, ans = 0, sum;
        max = static_cast<long>(pow(10, n)) - 1;
        min = max/10 + 1;
        sum = 2 * max;
        while (sum/2 * (sum - sum/2) > ans){
            long i = sum/2, j = sum - sum/2;
            while (j <= max && i >= min){
            	long num = i * j;
            	if (num > ans && isPalindrome(num)){
            		ans = num;
            		break;
            	}
            	i--;
            	j++;
            }
            sum--;
        }
        return ans % 1337;
    }
    bool isPalindrome(long x){
        long y = 0;
        for (long z = x; z != 0; y = 10 * y + z % 10, z /= 10);
        return x == y;
    }
};