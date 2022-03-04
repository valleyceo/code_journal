# LC 253. Meeting Rooms II

'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []

        for i in intervals:
            heapq.heappush(heap, (i[0], 1))
            heapq.heappush(heap, (i[1], -1))

        rooms = 0
        max_rooms = 0
        while heap:
            time = heapq.heappop(heap)
            rooms += time[1]
            max_rooms = max(max_rooms, rooms)

        return max_rooms
