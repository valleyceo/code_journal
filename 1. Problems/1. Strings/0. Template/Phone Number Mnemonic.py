# Phone number

'''
- given a dial number, return all possible character sequences
'''
# Time: O(4^n * n) - permutation takes O(4^n), base case takes O(n)
def phone_mnemonic(phone_number: str) -> List[str]:
    def phone_mnemonic_helper(digit: int) -> None:
        if digit == len(phone_number):
            # All digits are processed, so add partial_mnemonic to mnemonics.
            # (We add a copy since subsequent calls modify partial_mnemonic.)
            mnemonics.append(''.join(partial_mnemonic))
        else:
            # Try all possible characters for this digit.
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)

    mnemonics: List[str] = []
    partial_mnemonic = ['0'] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics
