#WAP to get the common data between two given lists.

a,b = eval(input("enter the list1?")),eval(input("enter the list2?"))

c = []

for i in a:
    if i in b:
        c.append(i)
print(c)
print(sorted(c))


