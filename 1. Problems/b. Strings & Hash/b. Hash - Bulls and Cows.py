# 299. Bulls and Cows

'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Constraints:

1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
'''
class Solution:
    # Optmial, O(n) time | O(1) space
    def getHint(self, secret: str, guess: str) -> str:
        mp = defaultdict(int)
        bulls = 0
        cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:

                if mp[secret[i]] < 0:
                    cows += 1

                if mp[guess[i]] > 0:
                    cows += 1

                mp[secret[i]] += 1
                mp[guess[i]] -= 1

        return "{}A{}B".format(bulls, cows)

    # O(n) time | O(n) space
    def getHint(self, secret: str, guess: str) -> str:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        bull = 0
        cow = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                continue

            d1[secret[i]] += 1
            d2[guess[i]] += 1

        for k in d1:
            if k in d2:
                cow += min(d1[k], d2[k])

        return str(bull) + "A" + str(cow) + "B"
