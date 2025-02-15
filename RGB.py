def sort_rgb():
    arr = list(input().split())
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 'B':  # Swap B to the front
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':  # Keep G in place
            mid += 1
        else:  # arr[mid] == 'R', Swap R to the end
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    print(" ".join(arr))  # Print without single quotes

sort_rgb()
