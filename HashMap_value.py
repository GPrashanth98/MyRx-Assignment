from collections import OrderedDict
from datetime import datetime
def sort_hashmap_by_value():
    n = int(input("Number of key-value pairs: "))
    data = {}
    for _ in range(n):
        key = int(input("Key: "))
        value = input("Value: ")
        data[key] = value
    
    sorted_items = sorted(data.items(), key=lambda x: x[1])
    print(OrderedDict(sorted_items))

sort_hashmap_by_value()