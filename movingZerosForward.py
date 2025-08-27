def movingZero(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
             
            pos += 1
            
    return arr

print(movingZero([0, 1, 0, 3, 12, 0, 5]))