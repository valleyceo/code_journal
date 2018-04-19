// Fizz Buzz

/*
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
*/

// my solution
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ans(n, "");
        int i = 1;
        
        while (i <= n) {
            if (i % 3 == 0) {
                ans[i-1] += "Fizz";
            }
            
            if (i % 5 == 0) {
                ans[i-1] += "Buzz";
            }
            
            if (ans[i-1].length() == 0) {
                ans[i-1] += to_string(i);
            }
            i++;
        }
        return ans;
    }
};