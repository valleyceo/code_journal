# LC 1554. Strings Differ by One Character

'''
Given a list of strings dict where all the strings are of the same length.

Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.

Example 1:

Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
'''

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        return self.rollingHash(dict)

    # O(MN) time | O(MN) space
    def maskMLE(self, dict: List[str]) -> bool:
        dset = set()

        for w in dict:
            for i in range(len(w)):
                mask = w[:i] + "*" + w[i+1:]

                if mask in dset:
                    return True

                dset.add(mask)

        return False

    # Rabin-Karp (rolling hash) O(MN) time | O(N + M) space
    def rollingHash(self, dict: List[str]) -> bool:
        mod = 10**9 + 7
        w_len = len(dict[0])
        hash_vals = []

        for w in dict:
            hash_val = 0

            for c in w:
                hash_val = (hash_val * 26 + ord(c) - ord('a')) % mod

            hash_vals.append(hash_val)

        power = 1

        for idx in reversed(range(w_len)):
            seen = set()

            for i, w in enumerate(dict):
                hash_val = (hash_vals[i] - (ord(w[idx]) - ord('a')) * power) % mod

                if hash_val in seen:
                    return True

                seen.add(hash_val)

            power = power * 26 % mod

        return False
