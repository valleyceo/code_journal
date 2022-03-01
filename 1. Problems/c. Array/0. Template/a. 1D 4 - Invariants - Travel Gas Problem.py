# Travel Gas Problem

'''
- Given circular cities with x gallons to fill and their distance
- Return the city (index) that is 'ample' (can make a full circle without getting empty)

- Assumes there always is an ample city
'''

MPG = 20

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.

# O(n) time | O(1) space
def find_ample_city(gallons: List[int], distances: List[int]) -> int:

    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas',
                                                 ('city', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(
                i, remaining_gallons)
    return city_remaining_gallons_pair.city
