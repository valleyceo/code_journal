# LC 1229. Meeting Scheduler

'''
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
'''
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        return self.solution2(slots1, slots2, duration)

    # O(NlogN + MlogM) time | O(1) space
    def solution1(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        idx1 = 0
        idx2 = 0

        while idx1 < len(slots1) and idx2 < len(slots2):

            start = max(slots1[idx1][0], slots2[idx2][0])
            end = min(slots1[idx1][1], slots2[idx2][1])

            if start < end and end - start >= duration:
                return [start, start + duration]

            if slots1[idx1][1] < slots2[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1

        return []

    # O((M+N)log(M+N)) time | O(M+N) space
    def solution2(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slot = []

        for s, e in slots1 + slots2:
            if e - s >= duration:
                slot.append([s, e])

        heapq.heapify(slot)

        while len(slot) > 1:
            s1, e1 = heapq.heappop(slot)
            s2, e2 = slot[0]

            if s2 + duration <= e1:
                return [s2, s2 + duration]

        return []
