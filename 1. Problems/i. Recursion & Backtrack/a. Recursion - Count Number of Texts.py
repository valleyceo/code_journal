# LC 2266. Count Number of Texts

'''
Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.


In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

For example, when Alice sent the message "bob", Bob received the string "2266622".
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.
'''

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        return self.topDown(pressedKeys)

    # O(N) time | O(N) space
    def topDown(self, pressedKeys: str) -> int:
        pmap = {"2": 3, "3": 3, "4": 3, "5": 3, "6": 3, "7": 4, "8": 3, "9": 4}
        mod = 10**9 + 7

        @lru_cache(None)
        def recurse(idx):
            if idx == len(pressedKeys):
                return 1

            res = 0

            for i in range(idx, len(pressedKeys)):
                if pressedKeys[i] != pressedKeys[idx]:
                    break

                count = i - idx

                if count >= pmap[pressedKeys[idx]]:
                    break

                count = recurse(i + 1)
                res += count

            return res % mod

        return recurse(0) % mod

    # O(N) time | O(N) space
    def bottomUp(self, pressedKeys: str) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * len(pressedKeys)

        for i in range(1, len(pressedKeys) + 1):
            dp[i] = dp[i-1] % mod

            if i - 2 >= 0 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] = (dp[i] + dp[i-2]) % mod

                if i - 3 >= 0 and pressedKeys[i-1] == pressedKeys[i-3]:
                    dp[i] = (dp[i] + dp[i-3]) % mod

                    if pressedKeys[i-1] in "79" and i - 4 >= 0 and pressedKeys[i-1] == pressedKeys[i-4]:
                        dp[i] = (dp[i] + dp[i-4]) % mod

        return dp[-1]
