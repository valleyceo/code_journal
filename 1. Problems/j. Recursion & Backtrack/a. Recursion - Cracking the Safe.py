# 753. Cracking the Safe

'''
There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].

The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.

For example, the correct password is "345" and you enter in "012345":
After typing 0, the most recent 3 digits is "0", which is incorrect.
After typing 1, the most recent 3 digits is "01", which is incorrect.
After typing 2, the most recent 3 digits is "012", which is incorrect.
After typing 3, the most recent 3 digits is "123", which is incorrect.
After typing 4, the most recent 3 digits is "234", which is incorrect.
After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.
Return any string of minimum length that will unlock the safe at some point of entering it.

Example 1:

Input: n = 1, k = 2
Output: "10"
Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.

Example 2:

Input: n = 2, k = 2
Output: "01100"
Explanation: For each possible password:
- "00" is typed in starting from the 4th digit.
- "01" is typed in starting from the 1st digit.
- "10" is typed in starting from the 3rd digit.
- "11" is typed in starting from the 2nd digit.
Thus "01100" will unlock the safe. "01100", "10011", and "11001" would also unlock the safe.

Constraints:

1 <= n <= 4
1 <= k <= 10
1 <= kn <= 4096
'''
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        return self.recursive(n, k)

    def recursive(self, n: int, k: int) -> str:

        def dfs(curr, visited):
            nonlocal max_nodes

            if len(visited) == max_nodes:
                return curr

            for i in range(k):
                tmp = curr[-(n-1):]+str(i) if n != 1 else(str(i))

                if tmp not in visited:
                    visited.add(tmp)
                    res = dfs(curr + str(i), visited)

                    if res:
                        return res

                    visited.remove(tmp)

        max_nodes = k**n
        return dfs("0"*n, set(["0"*n]))

    def nonrecursive(self, n: int, k: int) -> str:
        # start from 00000(k-1)
        prefix = '0' * (n-1)

        if n==1:
            return ''.join([str(x) for x in range(k)])
        if k == 1:
            return '0' * (n)

        prefix_dict = {}
        sequence = prefix

        for i in range(k**n):
            suffix = prefix_dict.get(prefix, k) - 1
            sequence += str(suffix)

            prefix_dict[prefix] = suffix
            prefix = prefix[1:] + str(suffix)

        return sequence

'''
Explanation:
- De Brujin sequence: You can create a chain sequence of all combinations (n, k) incrementing every idx.

ex: N: 2, k={0,1}
-> {0, 0, 1, 1} where sequence (0,0), (0,1), (1,1) is all substring
'''
