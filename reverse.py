n = input("enter the number")

l = list(n)
l.reverse()
reverse = ""
for i in l:
    reverse += i

print(int(reverse))


