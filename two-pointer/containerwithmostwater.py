def maxarea(arr):
    left = 0
    right = len(arr) - 1
    maxarea = 0
    while left < right:
        area = min(arr[left],arr[right])*(right -left)
        maxarea = max(area,maxarea)
        if arr[left] < arr[right]:
            left+=1
        else:
            right -= 1
    return maxarea
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxarea(height))