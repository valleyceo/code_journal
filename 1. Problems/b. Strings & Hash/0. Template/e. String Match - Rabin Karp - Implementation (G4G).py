# Rabin Karp Pattern Search Algorithm
# Source: GeeksforGeeks

# Number of characters in the input alphabet
d = 256

def search(pattern, text, hash):
    M = len(pattern)
    N = len(text)
    h = 1
    t = p = i = j = 0

    # The value of h would be "pow(d, M-1)% q"
    for i in range(M-1):
        h = (h * d)% q

    # Find hash value of pattern and first window
    for i in range(M):
        p = (d * p + ord(pattern[i]))% q
        t = (d * t + ord(text[i]))% q

    # Iterate for rest of text
    for i in range(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break

            j+= 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == M:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q

txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101 # Select a prime number
search(pat, txt, q)
