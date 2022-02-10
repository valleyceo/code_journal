// Next Closest Time

/*
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
*/

// my solution
class Solution {
public:
    
    string nextClosestTime(string time) {
        vector<int> digits;
        string new_time = time;
        
        // insert 4 digits
        digits.push_back(time[0]);
        digits.push_back(time[1]);
        digits.push_back(time[3]);
        digits.push_back(time[4]);
        
        // sort
        sort(digits.begin(), digits.end());
        
        // MINUTES
        // 1s
        int idx = 0;
        while (idx < digits.size() && new_time[4] >= digits[idx]) {
            idx++;
        }
        if (idx < digits.size() && new_time[4] != digits[idx]) {
            new_time[4] = digits[idx];
            return new_time;
        } else {
            new_time[4] = digits[0];
        }
        
        // 10s
        idx = 0;
        while (idx < digits.size() && new_time[3] >= digits[idx]) {
            idx++;
        }
        if (idx < digits.size() && new_time[3] != digits[idx] && digits[idx] < '6') {
            new_time[3] = digits[idx];
            return new_time;
        } else {
            new_time[3] = digits[0];
        }
        
        // HOURS
        // 1s
        idx = 0;
        while (idx < digits.size() && new_time[1] >= digits[idx]) {
            idx++;
        }
        if (idx < digits.size() && new_time[1] != digits[idx] && (new_time[0] < '2')) {
            new_time[1] = digits[idx];
            return new_time;
        } else if (idx < digits.size() && new_time[1] != digits[idx] && (new_time[0] == '2' && digits[idx] < '4')) {
            new_time[1] = digits[idx];
            return new_time;
        } else {
            new_time[1] = digits[0];
        }
        
        // 10s
        idx = 0;
        while (idx < digits.size() && new_time[1] >= digits[idx]) {
            idx++;
        }
        if (idx < digits.size() && new_time[1] != digits[idx] && (digits[idx] < '2' || (digits[idx] == '2' && new_time[1] < '4'))) {
            new_time[1] = digits[idx];
            return new_time;
        } else {
            new_time[1] = digits[0];
        }
        
        return new_time;
    }
};