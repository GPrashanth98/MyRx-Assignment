from collections import OrderedDict
from datetime import datetime
def sorted_squares():
    arr = list(map(int, input().split()))
    n = len(arr)
    left, right = 0, n - 1
    result = [0] * n
    pos = n - 1
    
    while left <= right:
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    
    print(result)

sorted_squares()