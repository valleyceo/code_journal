# LC 2271. Maximum White Tiles Covered by a Carpet

'''
You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.

Example 1:

Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10.
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
'''
# O(nlogn) time | O(n) space
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        return self.prefixSumBinarySearch(tiles, carpetLen)

    def prefixSumBinarySearch(self, tiles: List[List[int]], carpetLen: int) -> int:
        n = len(tiles)
        tiles.sort()

        tile_start_list = [tile[0] for tile in tiles]
        prefix_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + (tiles[i - 1][1] - tiles[i - 1][0] + 1)

        res = 0

        for i, tile in enumerate(tiles):
            s, e = tile

            if e - s + 1 >= carpetLen:
                return carpetLen

            end_idx = bisect_right(tile_start_list, s + carpetLen - 1) - 1
            compensate = 0

            if tiles[end_idx][1] - s + 1 > carpetLen:
                compensate = tiles[end_idx][1] - s + 1 - carpetLen

            res = max(res, prefix_sum[end_idx + 1] - prefix_sum[i] - compensate)

        return res
