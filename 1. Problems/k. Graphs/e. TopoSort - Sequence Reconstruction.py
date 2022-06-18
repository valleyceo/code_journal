# LC 444. Sequence Reconstruction

'''
You are given an integer array nums of length n where nums is a permutation of the integers in the range [1, n]. You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.

Check if nums is the shortest possible and the only supersequence. The shortest supersequence is a sequence with the shortest length and has all sequences[i] as subsequences. There could be multiple valid supersequences for the given array sequences.

For example, for sequences = [[1,2],[1,3]], there are two shortest supersequences, [1,2,3] and [1,3,2].
While for sequences = [[1,2],[1,3],[1,2,3]], the only shortest supersequence possible is [1,2,3]. [1,2,3,4] is a possible supersequence but not the shortest.
Return true if nums is the only shortest supersequence for sequences, or false otherwise.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
Output: false
Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
The sequence [1,2] is a subsequence of both: [1,2,3] and [1,3,2].
The sequence [1,3] is a subsequence of both: [1,2,3] and [1,3,2].
Since nums is not the only shortest supersequence, we return false.
'''
# Kahn's Algorithm, O(V + E) time | O(V) space
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        nodes = set()

        for seq in sequences:
            for n in seq:
                nodes.add(n)

        graph = {x: [] for x in nodes}
        indegrees = {x: 0 for x in nodes}

        for seq in sequences:
            for i in range(1, len(seq)):
                graph[seq[i-1]].append(seq[i])
                indegrees[seq[i]] += 1

        queue = deque()

        for node, in_deg in indegrees.items():
            if in_deg == 0:
                queue.append(node)

        if len(queue) != 1:
            return False

        res = []

        while queue:
            if len(queue) > 1:
                return False

            node = queue.pop()
            res.append(node)

            for next_node in graph[node]:
                indegrees[next_node] -= 1

                if indegrees[next_node] == 0:
                    queue.append(next_node)

        return len(nodes) == len(res) and res == nums
