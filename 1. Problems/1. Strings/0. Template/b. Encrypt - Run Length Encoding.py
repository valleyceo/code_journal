# Run Length encoding

'''
- encode ex: "aaaabcccaa" -> "4a1b3c2a"
- decode ex: "3e4f2e" -> "eeeffffee"
'''
def decoding(s: str) -> str:

    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            result.append(c * count)
            count = 0
    return ''.join(result)


def encoding(s: str) -> str:

    result, count = [], 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            result.append(str(count) + s[i - 1])
            count = 1
        else:
            count += 1
    return ''.join(result)
