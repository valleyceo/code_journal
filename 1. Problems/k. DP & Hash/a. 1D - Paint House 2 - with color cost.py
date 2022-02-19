# LC 265. Paint House 2

'''
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.

Example 1:

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

Example 2:

Input: costs = [[1,3],[2,4]]
Output: 5

Constraints:

costs.length == n
costs[i].length == k
1 <= n <= 100
2 <= k <= 20
1 <= costs[i][j] <= 20

Follow up: Could you solve it in O(nk) runtime?
'''
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        return self.optimal(costs)
        
    def mySolution(Self, cost: List[List[int]]) -> int:
        for r in range(1, len(costs)):
            for i in range(len(costs[0])):
                minVal = sys.maxsize
                
                for j in range(len(costs[0])):
                    if i == j:
                        continue
                    
                    minVal = min(minVal, costs[r-1][j])
                costs[r][i] += minVal
                
        return min(costs[-1])
    
    
    def optimal(self, costs: List[List[int]]) -> int:
        
        firstMin = [sys.maxsize, -1]
        secondMin = [sys.maxsize, -1]
        rows = len(costs)
        cols = len(costs[0])
        
        for i in range(cols):
            if costs[0][i] <= firstMin[0]:
                secondMin = firstMin
                firstMin = [costs[0][i], i]
            elif costs[0][i] < secondMin[0]:
                secondMin = [costs[0][i], i]
                
        for i in range(1, rows):
            nextFirstMin = [sys.maxsize, -1]
            nextSecondMin = [sys.maxsize, -1]

            for j in range(cols):
                cost = costs[i][j]
                if firstMin[1] != j:
                    cost += firstMin[0]
                else:
                    cost += secondMin[0]
                
                if cost <= nextFirstMin[0]:
                    nextSecondMin = nextFirstMin
                    nextFirstMin = [cost, j]
                elif cost < nextSecondMin[0]:
                    nextSecondMin = [cost, j]
                
            firstMin = nextFirstMin
            secondMin = nextSecondMin
                
        return firstMin[0]