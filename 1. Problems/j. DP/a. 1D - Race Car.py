# LC 818. Race Car

'''
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.
'''
class Solution:
    def racecar(self, target: int) -> int:
        return self.bfsSolution(target)

    def bfsSolution(self, target: int) -> int:
        queue = [(0, 1)]
        count = 0
        visited = {(0, 1)}

        while queue:
            next_queue = []

            for pos, speed in queue:
                next_pos = pos + speed
                next_speed = speed * 2

                if pos == target:
                    return count
                elif pos < 0 or pos > 20000:
                    continue

                if (next_pos, next_speed) not in visited:
                    next_queue.append((next_pos, next_speed))
                    visited.add((next_pos, next_speed))

                if speed > 0 and (pos, -1) not in visited:
                    next_queue.append((pos, -1))
                    visited.add((pos, -1))
                elif speed < 0 and (pos, 1) not in visited:
                    next_queue.append((pos, 1))
                    visited.add((pos, 1))

            queue = next_queue
            count += 1

        return -1

    def bitMask(self, target: int) -> int:
        dp = {0: 0}

        def helper(t):
            print(t, bin(t))
            if t in dp:
                return dp[t]

            n = t.bit_length()

            if 2**n - 1 == t:
                dp[t] = n
            else:
                dp[t] = helper(2**n - 1 - t) + n + 1

                for i in range(n - 1):
                    dp[t] = min(dp[t], helper(t - 2**(n - 1) + 2**i) + n + i + 1)

            return dp[t]

        return helper(target)
