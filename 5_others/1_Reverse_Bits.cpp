// Reverse Bits

/*
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
*/

// my solution
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        string tmp = "";
        for (int i = 31; i >= 0; i--) {
            tmp.push_back((n%2) + '0');
            n >>= 1;
        }
        
        bitset<32> bVal(tmp);
        return bVal.to_ulong();
    }
};