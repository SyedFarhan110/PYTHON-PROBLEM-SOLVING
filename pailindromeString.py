def pail(word):
    j = len(word) -1 
    for i in range(len(word)//2):
        if word[i] != word[j - i]:
            return False
    return True
print(pail("civic"))
        