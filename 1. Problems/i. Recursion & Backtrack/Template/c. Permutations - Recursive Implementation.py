pList = []

def permute(idx, arr):
    if idx == len(arr):
        pList.append(arr[:])
        return

    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        permute(idx + 1, arr)
        arr[idx], arr[i] = arr[i], arr[idx]

nums = [1,2,3,4,5]
permute(0, nums)
print(pList)
