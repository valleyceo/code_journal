# Compute an Optimum Assignment of Tasks

'''
- Given a list of tasks with duration time, and each worker must take two tasks
- Return the optimum duration to complete all
'''
PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

# O(nlogn) time
def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:

    task_durations.sort()
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations) // 2)
    ]
