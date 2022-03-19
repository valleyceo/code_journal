# Render a Calendar

'''
- Given a set of event times
- Find the maximum number of events that takes place concurrently
'''

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# O(nlogn) time | O(n) space
def find_max_simultaneous_events(A: List[Event]) -> int:

    # Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
    # are equal, start_time comes first
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    # Builds an array of all endpoints.
    E = [
        p for event in A
        for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.
    E.sort(key=lambda e: (e.time, not e.is_start))

    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events,
                                              max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events
