# Remove First-Name Duplicates

'''
- Design an efficient algorithm for removing all first-name duplicates from an array.
'''

# O(nlogn) time | O(1) space
class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __eq__(self, other) -> bool:
        return self.first_name == other.first_name

    def __lt__(self, other) -> bool:
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)


def eliminate_duplicate(A: List[Name]) -> None:

    A.sort()  # Makes identical elements become neighbors.
    write_idx = 1
    for cand in A[1:]:
        if cand != A[write_idx - 1]:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx:]
