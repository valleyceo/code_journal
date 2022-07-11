# Design a Rate Limiting System

'''
A Rate Limiting System can allow a maximum of n requests every t seconds, using an implementation similar to the sliding window algorithm.

Given two positive integers n and t, and a non-decreasing stream of integers representing the timestamps of requests, implement a data structure that can check if each request is allowed or not.

Implement the RateLimiter class:

RateLimiter(int n, int t) Initializes the RateLimiter object with an empty stream and two integers n and t.
boolean shouldAllow(int timestamp) Returns true if the current request with timestamp timestamp is allowed, otherwise returns false. Note that while checking if the current request should be allowed, only the timestamps of requests previously allowed are considered.
'''

class RateLimiter:

    def __init__(self, n: int, t: int):
        self.queue = deque()
        self.capacity = n
        self.time = t

    def shouldAllow(self, timestamp: int) -> bool:

        while self.queue and self.queue[0] <= (timestamp - self.time):
            self.queue.popleft()

        if len(self.queue) < self.capacity:
            self.queue.append(timestamp)
            return True

        return False
