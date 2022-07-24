# LC 1776. Car Fleet II

'''
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
'''

# O(n) time | O(n) space
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        return self.monoStack(cars)

    def bruteForce(self, cars: List[List[int]]) -> List[float]:
        res = []

        for i in range(len(cars)):
            min_time = float('inf')

            for j in range(len(cars) - 1, i, -1):

                if cars[i][1] > cars[j][1]:
                    time = (cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1])
                    min_time = min(min_time, time)

            if min_time == float('inf'):
                res.append(-1)
            else:
                res.append(min_time)

        return res

    def monoStack(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stack = []
        res = [-1] * n

        for i in range(n - 1, -1, -1):
            p, s = cars[i]

            while stack and (cars[stack[-1]][1] >= s or (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()

            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])

            stack.append(i)

        return res

"""
Note:
- Monostack with two parameters,
- On top of popping higher speed, you want to pop the higher time too.
    - Ex: [[3,4], [6,3],[9,1]] -> [3,4] to [9,1] is shorter time than [3,4] to [6,3]
"""
