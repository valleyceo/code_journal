# Find Anagrams

# O(nm * log(m))
def find_anagrams(dictionary):
    a_dict = collections.defaultdict(list)

    for s in dictionary:

        a_dict["".join(sorted(s))].append(s)

    return [x for x in a_dict.values() if len(x >= 2)]
