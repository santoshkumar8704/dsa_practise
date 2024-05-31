def removedup(arr):
    slow = 0
    for fast in range(1,len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
            
    return arr

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = removedup(nums)
print(new_length)