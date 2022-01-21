
n = eval(input("enter the value:"))

def fibonacci(n):
    a = 0
    b = 1
    print(a,b,end=" ")

    for i in range(2,n):
        c = a + b
        print(c,end= " " )
        a = b
        b = c
        n = n + 1

fibonacci(n)

