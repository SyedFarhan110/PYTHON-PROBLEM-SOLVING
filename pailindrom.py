def pail(n):
    reverse = 0
    m = n
    while n > 0:
        digit = n % 10
        reverse = reverse *10 + digit
        n = n // 10
    print(reverse)
    if reverse == m:
        return True
    else:
        return False
    
print(pail(12121))