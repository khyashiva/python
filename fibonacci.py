n = eval(input("> "))
sum = 0

#0 1 1 2 3 5 7

for i in range(n):
    if i == 0:
        a = i
        print(a,end=" ")
    elif i == 1:
        b = i
        print(b,end=" ")
    else:
        sum = a + b
        print(sum,end = " ")
        a = b
        b = sum





