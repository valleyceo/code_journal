// 1-bit and 2-bit Characters

/*
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
*/

// my solution
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        if (bits[bits.size()-1] == 1) return false;
        
        int check = bits.size() - 2;
        int count = 0;
        
        while (bits[check--] != 0)
            count++;
        
        return (count % 2 == 0) ? true : false;
    }
};