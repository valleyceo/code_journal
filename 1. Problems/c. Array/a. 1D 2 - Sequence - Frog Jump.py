# LC 403. Frog Jump

'''
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
'''

# O(N^2) time | O(N^2) space
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        return self.bottomUp(stones)

    def topDown(self, stones: List[int]) -> bool:
        last_stone = stones[-1]
        stone_set = set(stones)

        if stones[0] + 1 not in stone_set:
            return False

        @lru_cache(None)
        def traverse(step, speed):
            if step == last_stone:
                return True

            for next_speed in [speed-1, speed, speed+1]:
                if next_speed == 0 or step + next_speed not in stone_set:
                    continue

                if traverse(step+next_speed, next_speed):
                    return True

            return False

        return traverse(1, 1)

    def bottomUp(self, stones: List[int]) -> bool:

        last_stone = stones[-1]
        stone_set = set(stones)
        dp = defaultdict(set)
        dp[stones[0]].add(0) # This cleans up all edge cases

        for step in stones:
            for speed in dp[step]:

                for next_speed in [speed - 1, speed, speed + 1]:
                    if next_speed == 0 or step + next_speed not in stone_set:
                        continue

                    if step + next_speed == last_stone:
                        return True

                    dp[step + next_speed].add(next_speed)

        return False
