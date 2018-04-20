// Meeting Rooms II

/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
*/

// my solution
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if (intervals.size() == 0) {
            return 0;
        }
        
        map<int, int> map;
        
        for (auto interval : intervals) {
            map[interval.start]++;
            map[interval.end]--;
        }
        
        int count = 0;
        int result = 0;
        
        for (auto it = map.begin(); it != map.end(); ++it) {
            count = count + it->second;
            result = max(result, count);
        }
        
        return result;
    }
};