# Schedule to Minimize Waiting Time (need to review)

'''
- Given a set of query waiting time
- Create schedule for a minimal processing time

- Example: <2,5,1,3> -> 10 (optimal when 0 + (1) + (1+2) + (1+2+3))
'''

# O(nlogn) time
def minimum_total_waiting_time(service_times: List[int]) -> int:

    # Sort the service times in increasing order.
    service_times.sort()
    total_waiting_time = 0
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries
    return total_waiting_time


def minimum_total_waiting_time_pythonic(service_times):
    return sum(
        remaining_queries * time
        for remaining_queries, time in enumerate(sorted(service_times)[::-1]))
