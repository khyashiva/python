def facto(n):
    if n==0: return 1 # base condition
    return n*facto(n-1) # recursive condition
print(facto(5))

