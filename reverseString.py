def reverseString(sentence):
    word = ''
    result = []
    for i in sentence:
        if i != " ":
            word += i
        else:
            result.append(word)
            word = ''
    result.append(word)
    result = result[:: -1]
    return ' '.join(result)

print(reverseString("hello how are"))

