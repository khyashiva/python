n = eval(input("enter the number:"))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
sum = 1
for i in range(1,n+1):
    sum = sum * i
print(sum)

print(factorial(n))


