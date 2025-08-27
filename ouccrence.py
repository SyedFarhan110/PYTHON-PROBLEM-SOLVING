def occurence(arr):
    dict = {}
    for i in arr.lower():
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(occurence("farhanF"))