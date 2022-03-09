# T1 - EXACT MATCH SEARCH
'''
NOTE: Used for searching a exact condition
'''

left = 0
right = N - 1

while left <= right:
    mid = left + (right - left) / 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid

# TEMPLATE 2 - BOUND SEARCH
'''
NOTE: Used for searching lower/upper bound
'''

# LOWER BOUND
left = 0
right = N

while left < right:
    mid = left + (right - left) / 2

    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid

# UPPER BOUND
left = 0
right = N - 1

while left < right:
    mid = left + (right - left + 1) // 2

    if nums[mid] <= target:
        left = mid
    else:
        right = mid - 1

# T3 - FIND NEXT TO BOUND
'''
NOTE: Used for immediate neighber of lower bound
'''
left = 0
right = N - 1

while left + 1 < right:
    mid = left + (right - left) / 2

    if nums[mid] < target:
        left = mid
    else:
        right = mid
