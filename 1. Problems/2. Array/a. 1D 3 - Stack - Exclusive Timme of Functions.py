# LC 636. Exclusive Time of Functions

'''
Given sequence of order of [ID, action, TimmeStamp], return time for each ID. IDs are nodes of 0, 1, ..., n. Actions are only "Start" and "End". Sequences are time ordered.

Example 1:
Input: 
n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

Output: 
[3,4]

Example 2:
Input: 
n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]

Output: 
[8]

Example 3:
Input: 
n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]

Output: 
[7,1]

Constraints:

1 <= n <= 100
1 <= logs.length <= 500
0 <= function_id < n
0 <= timestamp <= 109
No two start events will happen at the same timestamp.
No two end events will happen at the same timestamp.
Each function has an "end" log for each "start" log.
'''