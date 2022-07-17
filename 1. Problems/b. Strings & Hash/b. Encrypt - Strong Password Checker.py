# LC 420. Strong Password Checker

'''
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
'''

# O(N) time | O(1) space
class Solution:
    def strongPasswordChecker(self, password: str) -> int:

        missing_type = [True] * 3

        for c in password:
            if "a" <= c <= "z":
                missing_type[0] = False
            elif "A" <= c <= "Z":
                missing_type[1] = False
            elif c.isdigit():
                missing_type[2] = False

        to_add = sum(missing_type)
        to_change = 0
        one = 0
        two = 0
        idx = 2

        while idx < len(password):
            if password[idx] == password[idx - 1] == password[idx - 2]:
                length = 3

                while idx + 1 < len(password) and password[idx + 1] == password[idx]:
                    idx += 1
                    length += 1

                to_change += length // 3

                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1

            idx += 1

        if len(password) < 6:
            return max(to_add, 6 - len(password))
        elif len(password) <= 20:
            return max(to_add, to_change)
        else:
            to_delete = len(password) - 20

            to_change -= min(to_delete, one)
            to_change -= min(max(to_delete - one, 0), two * 2) // 2
            to_change -= max(to_delete - one - 2 * two, 0) // 3

        return to_delete + max(to_add, to_change)
