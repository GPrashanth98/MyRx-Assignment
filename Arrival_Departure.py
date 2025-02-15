def min_platforms():
    arrivals = input().split()
    departures = input().split()
    
    arr = sorted([int(a.replace(':', '')) for a in arrivals])
    dep = sorted([int(d.replace(':', '')) for d in departures])
    
    platforms, max_platforms, i, j = 0, 0, 0, 0
    
    while i < len(arr) and j < len(dep):
        if arr[i] < dep[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    
    print(max_platforms)

min_platforms()