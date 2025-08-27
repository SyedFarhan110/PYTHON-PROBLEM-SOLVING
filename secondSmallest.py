def secondSmallest(arr):
    # smallest = arr[0]
    # s_smallest = arr[1]
    # for i in arr:
    #     if i < smallest:
    #         s_smallest = smallest
    #         smallest = i
    #     elif i < s_smallest and i != smallest:
    #         s_smallest = i
    # return s_smallest

# print(secondSmallest([1, 3, 4, 5, 2]))
    smallest = arr[0]
    s_smallest = arr[1]
    for i in arr:
        if i < smallest:
            s_smallest = smallest
            smallest = i
        elif i < s_smallest and i != smallest:
            s_smallest = i
    return s_smallest

print(secondSmallest([1, 3, 4, 5, 2]))