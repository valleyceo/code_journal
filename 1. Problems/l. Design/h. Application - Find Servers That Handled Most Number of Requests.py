# LC 1606. Find Servers That Handled Most Number of Requests

'''
You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

The ith (0-indexed) request arrives.
If all servers are busy, the request is dropped (not handled at all).
If the (i % k)th server is available, assign the request to that server.
Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.
'''
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        freq = [0] * k
        busy = []
        free = SortedList([i for i in range(k)])

        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, server = heapq.heappop(busy)
                free.add(server)

            if free:
                fi = free.bisect_left(i % k) % len(free)
                server = free.pop(fi)
                freq[server] += 1
                heappush(busy, (a + l, server))

        max_freq = max(freq)
        return [i for i, x in enumerate(freq) if x == max_freq]

"""
NOTE:
- resource: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/discuss/1089184/Python3-summarizing-3-approaches
"""
