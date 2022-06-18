# LC 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

'''
Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

A binary matrix is a matrix with all cells equal to 0 or 1 only.

A zero matrix is a matrix with all cells equal to 0.
'''
# O(2^(MN)) time | O(2^(MN)) space
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        def flip(i, j, M):
            M2 = copy.deepcopy(M)

            for i2, j2 in [[i, j], [i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    M2[i2][j2] ^= 1

            return M2

        def createKey(M):
            s = ""

            for i in range(m):
                for j in range(n):
                    s += str(M[i][j])

            return s

        key = createKey(mat)
        visited = {key}
        queue = deque([[mat, 0]])

        while queue:
            curr_mat, curr_count = queue.popleft()

            if sum(map(sum, curr_mat)) == 0:
                return curr_count

            for i in range(m):
                for j in range(n):
                    next_mat = flip(i, j, curr_mat)
                    key = createKey(next_mat)

                    if key in visited:
                        continue

                    queue.append([next_mat, curr_count + 1])
                    visited.add(key)

        return -1
