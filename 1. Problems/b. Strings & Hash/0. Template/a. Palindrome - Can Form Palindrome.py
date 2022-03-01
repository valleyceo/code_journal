# Palindrome Permuations

'''
- Given a string of letters
- Test if the string can be permuted to form a palindrome

- Example: "edified" -> "deified"
'''

def can_form_palindrome(s: str) -> bool:

    # A string can be permuted to form a palindrome if and only if the number
    # of chars whose frequencies is odd is at most 1.
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


'''
- Time complexity: O(n)
- Space complexity: O(c), where c is the number of distinct characters
'''
