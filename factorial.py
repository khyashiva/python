#factorial

n = eval(input("> "))
def fact(n):
    if n < 0:
        return "invalid"
    elif n == 0:
        return 1
    return n*fact(n-1)

print(fact(n))


