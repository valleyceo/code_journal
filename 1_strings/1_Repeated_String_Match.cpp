// Repeated String Match

/*
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
*/

// my solution -- Tried: 4, Time: 30 min, can be shortened
class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        int alen = A.length();
        string Anew = A;
        int ct = 1;
        
        // check if B is already a substring
        size_t found = Anew.find(B);
        if (found != string::npos)
            return ct;
        
        while (alen < B.length()) {
            Anew += A;
            alen += A.length();
            ct++;
        }
        
        // check if B is substring
        found = Anew.find(B);
        if (found != string::npos)
            return ct;
        
        // check 1 more after loop
        Anew += A;
        alen += A.length();
        ct++;
        
        // check if B is substring of Anew
        found = Anew.find(B);
        if (found != string::npos) {
            return ct;
        } else {
            return -1;
        }
    }
};