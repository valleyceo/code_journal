# Generate Palindromic Decomposition

'''
- Given a string of characters
- Compute all possible decomposition
- Example: "611116" -> one case is "611", "11", "6"
'''
# O(N x 2^N) time
# Same complexity as brute force, but much better best-case (when there are fewer palindromic decomposition)
def palindrome_decompositions(text: str) -> List[List[str]]:
    def directed_palindrome_decompositions(offset, partial_partition):
        if offset == len(text):
            result.append(partial_partition.copy())
            return

        for i in range(offset + 1, len(text) + 1):
            prefix = text[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(
                    i, partial_partition + [prefix])

    result: List[List[str]] = []
    directed_palindrome_decompositions(offset=0, partial_partition=[])
    return result


# Pythonic solution uses bottom-up construction.
def palindrome_decompositions_pythonic(text: str) -> List[List[str]]:
    return ([[text[:i]] + right
             for i in range(1,
                            len(text) + 1) if text[:i] == text[:i][::-1]
             for right in palindrome_decompositions_pythonic(text[i:])]
            or [[]])
