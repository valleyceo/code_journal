# Transform One String to Another (need to review, no idea)

'''
- Given a dictionary D and two strings s and t
- Determine if s produces t
'''
# O(n^2) time
def transform_string(D: Set[str], s: str, t: str) -> int:

    StringWithDistance = collections.namedtuple(
        'StringWithDistance', ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)  # Marks s as visited by erasing it in D.

    while q:
        f = q.popleft()
        # Returns if we find a match.
        if f.candidate_string == t:
            return f.distance  # Number of steps reaches t.

        # Tries all possible transformations of f.candidate_string.
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:  # Iterates through 'a' ~ 'z'.
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1  # Cannot find a possible transformations.


def transform_string_pythonic(D, s, t):
    if s == t:
        return 0
    length = 1
    running = set([s])
    while running:
        running = D & set(cand[:i] + c + cand[i + 1:] for cand in running
                          for i in range(len(cand))
                          for c in string.ascii_lowercase)
        if t in running:
            return length
        length += 1
        D -= running
    return 0
