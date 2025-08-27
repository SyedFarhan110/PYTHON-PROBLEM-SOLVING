def twoSum(arr, target):
    array_set = set(arr)
    for i in array_set:
        if (target - i) in array_set and i != target - i:
            return i, target - i
        
print(twoSum([2,3,5,7], 6))