# LC 659. Split Array into Consecutive Subsequences

'''
You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5

Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
'''
class Solution:

    def isPossible(self, nums: List[int]) -> bool:
        return self.optimizedSolution(nums)

    # O(n) time | O(n) space
    def optimizedSolution(self, nums: List[int]) -> bool:
        left = Counter(nums)
        end_pointer = Counter()

        for n in nums:
            if not left[n]:
                continue

            left[n] -= 1

            if end_pointer[n - 1] > 0:
                end_pointer[n - 1] -= 1
                end_pointer[n] += 1

            elif left[n + 1] and left[n + 2]:
                left[n + 1] -= 1
                left[n + 2] -= 1
                end_pointer[n + 2] += 1
            else:
                return False

        return True

"""
Insight:
* You cannot check for more maximum sequence (ex: [1,2,3,3,4,4,5] -> [1,2,3,4,5], [3,4] is wrong)
- You still can solve greedily:
    - Create a counter and a last seq poimarkernter.
    - For each number sequence, if there is a prior sequence then add it
    - If not, then create a new sequence (check if beginning sequence is larger than 2)

- Why do you need a prev seq marker?
    - Because seq needs to stop at 3 and see if new array is formed (ex. [1, 2, 3, 3, 4, 5]).
    - Checking new sequence comes first, and checking prev marker comes first on next iteration
"""
