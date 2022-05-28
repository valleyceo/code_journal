# LC 2184. Number of Ways to Build Sturdy Brick Wall

'''
You are given integers height and width which specify the dimensions of a brick wall you are building. You are also given a 0-indexed array of unique integers bricks, where the ith brick has a height of 1 and a width of bricks[i]. You have an infinite supply of each type of brick and bricks may not be rotated.

Each row in the wall must be exactly width units long. For the wall to be sturdy, adjacent rows in the wall should not join bricks at the same location, except at the ends of the wall.

Return the number of ways to build a sturdy wall. Since the answer may be very large, return it modulo 109 + 7.
'''

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        return self.precompute(height, width, bricks)

    def backtrackTLE(self, height: int, width: int, bricks: List[int]) -> int:
        cache = {}
        mod = 10**9 + 7
        bricks.sort()

        def backtrack(w, h, prev_gap, curr_gap):

            if w > width or h > height:
                return 0

            if w == width and h == height:
                return 1

            key = (w, h, prev_gap, curr_gap)

            if key in cache:
                return cache[key]

            if w == width:
                return backtrack(0, h + 1, curr_gap, 0)

            count = 0

            for b in bricks:
                if w + b < width and (1 << (w+b)) & prev_gap:
                    continue

                if w + b > width:
                    break

                count = (count + backtrack(w + b, h, prev_gap, curr_gap | (1 << w+b))) % mod

            cache[key] = count
            return count

        return backtrack(0, 1, 0, 0)

    def precompute(self, height: int, width: int, bricks: List[int]) -> int:
        ways = []
        mod = 10**9 + 7
        bricks.sort()

        def backtrack(w, mask):

            for b in bricks:
                if w + b > width:
                    break

                if w + b == width:
                    ways.append(mask)
                    break

                backtrack(w + b, mask | (1 << w + b))

        backtrack(0, 0)
        possible_seq = defaultdict(list)

        for way in ways:
            for way2 in ways:
                if way & way2  == 0:
                    possible_seq[way].append(way2)

        prev = {way: 1 for way in ways}

        for i in range(1, height):
            curr = {}

            for way in ways:
                curr[way] = 0

                for way2 in possible_seq[way]:
                    curr[way] = (curr[way] + prev[way2]) % mod

            prev = curr

        return sum(prev.values()) % mod
