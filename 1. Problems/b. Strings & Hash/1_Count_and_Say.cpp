// Count and Say

/*
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
*/

// time: O(2^n * n)
// Explanation: if all numbers are different, string can double at max (2^n). Also, the iteration is run n times (n).
// my solution - optimal
class Solution {
public:
    string countAndSay(int n) {
        char digits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
        int itr = 1;
        string seq = "1";

        while (itr++ < n) {
            char num = seq[0];
            string new_seq = "";

            int ct = 1;

            for (int i = 1; i < seq.length(); i++) {
                if (seq[i] == num) {
                    ct += 1;
                } else {
                    new_seq += digits[ct];
                    new_seq += num;

                    num = seq[i];
                    ct = 1;
                }
            }

            // last iteration
            new_seq += digits[ct];
            new_seq += num;

            seq = new_seq;
        }

        return seq;
    }
};
