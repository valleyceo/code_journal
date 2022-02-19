# Partitioning and Sorting an Array with Many Repeated Entries

'''
- Given an array of student objects with integer-valued age as key
- Rearrange the elements of the array so that the students of equal age appear together (does not have to be age ordered)
'''

Person = collections.namedtuple('Person', ('age', 'name'))

# O(n) time | O(m) space, m is number of distinct ages
# Can avoid O(m) space by performing in-place
def group_by_age(people: List[Person]) -> None:

    age_to_count = collections.Counter((person.age for person in people))
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[people[from_idx].age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        # Use age_to_count to see when we are finished with a particular age.
        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]
