// Repeated String Match

/*
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

could be in two cases (second case needs extra loop)
*/

// my solution -- Tried: 4, Time: 30 min
class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        int alen = A.length();
        string Anew = A;
        int repeat = 1;
        
        while (Anew.length() < B.length()) {
            Anew += A;
            repeat += 1;
        }
        
        if (Anew.find(B) != string::npos) return repeat;
        
        Anew += A;
        repeat += 1;
        
        if (Anew.find(B) != string::npos) return repeat;
        
        return -1;
    }
};