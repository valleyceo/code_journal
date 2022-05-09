# LC 1024. Video Stitching

'''
You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.

Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.

We can cut these clips into segments freely.

For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

Example 2:

Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation: We cannot cover [0,5] with only [0,1] and [1,2].
'''

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        return self.optimizedSpace(clips, time)

    # O(nlogn) time | O(n + t) space
    def dpSolution(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        dp = [0] + [time + 1] * time

        for clip in clips:
            for j in range(max(clip[0], 0), min(clip[1], time) + 1):
                dp[j] = min(dp[j], dp[max(clip[0], 0)] + 1)

        return dp[time] if dp[time] < time + 1 else -1

    # O(nlogn) time | O(n) space
    def optimizedSpace(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        prev_furthest = -1
        furthest = 0
        res = 0

        for clip in clips:

            if furthest >= time or clip[0] > furthest: # video time is fully covered or cannot be covered
                break
            elif prev_furthest < clip[0]:
                res += 1
                prev_furthest = furthest

            furthest = max(furthest, clip[1])

        return res if furthest >= time else -1
