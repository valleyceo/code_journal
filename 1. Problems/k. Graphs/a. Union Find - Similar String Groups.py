# 839. Similar String Groups

'''
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
'''
# O(N^2 * S) time complexity | O(N) space complexity, S is the length of string
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            diff_count = 0

            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff_count += 1

                if diff_count > 2:
                    return False

            return True

        def find(x, root):
            if root[x] != x:
                root[x] = find(root[x], root)

            return root[x]

        def union(x, y, root):
            rx = find(x, root)
            ry = find(y, root)

            if rx != ry:
                if rx < ry:
                    root[ry] = rx
                else:
                    root[rx] = ry

        n = len(strs)
        uf_root = [i for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    union(i, j, uf_root)

        roots = set()

        for i in range(n):
            roots.add(find(i, uf_root))

        return len(roots)
