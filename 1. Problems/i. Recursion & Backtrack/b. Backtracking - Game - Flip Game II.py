# LC 294. Flip Game II

'''
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return true if the starting player can guarantee a win, and false otherwise. 

Example 1:

Input: currentState = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Example 2:

Input: currentState = "+"
Output: false
'''

class Solution:
    @lru_cache(None)
    def canWin(self, currentState: str) -> bool:

        for i in range(1, len(currentState)):
            if currentState[i-1:i+1] == "++":
                if not self.canWin(currentState[:i-1] + "--" + currentState[i+1:]):
                    return True

        return False
