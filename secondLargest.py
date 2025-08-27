def secondLargest(arr):
    largest = arr[0]
    s_largest = arr[1]
    
    for i in arr:
        if i > largest:
            s_largest = largest
            largest = i
        elif i > s_largest and i != largest:
            s_largest = i
    return s_largest
        
print(secondLargest([1, 3, 4, 5, 2]))


