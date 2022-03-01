# Compute Buildings with a Sunset View

'''
- Given a sequence of buildings
- Return index of buildings that can see the sunset (east to west)
- Input: [3, 5, 3, 2, 4]
- Output: [1(5), 4(4)]
'''
# O(n) time | O(n) space
def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:

    BuildingWithHeight = collections.namedtuple('BuildingWithHeight',
                                                ('id', 'height'))
    candidates: List[BuildingWithHeight] = []

    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [c.id for c in reversed(candidates)]
