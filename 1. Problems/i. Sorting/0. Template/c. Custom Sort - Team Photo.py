# Valid Photoshot Standing

'''
- Given 2 rows of arrays of same size,
- Check if it is possible to arrange each arrays s.t. each elements in row 1 is bigger than the row 2 (of same column)
'''

# O(nlogn) time
class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height: List[int]) -> None:
        self._players = [Team.Player(h) for h in height]

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0: 'Team', team1: 'Team') -> bool:

        return all(
            a < b
            for a, b in zip(sorted(team0._players), sorted(team1._players)))
