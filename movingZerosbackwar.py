def moving(arr):
    pos = len(arr) - 1
    for i in range(len(arr) -1, -1, -1):
        if(arr[i] != 0 ):
            arr[pos], arr[i] = arr[i], arr[pos]
            pos -= 1
    return arr

print(moving([0, 1, 0, 3, 12, 0, 5]))