"""

WAP to get the common data between two given lists.
[1, 2, 3, 4], [4, 3, 5, 6, 7] --> [3, 4]
"""

a = eval(input("1? "))
b = eval(input("2?"))
c = []
print(type(c))

for i in a:
    if i in b:
        c.append(i)
print(sorted(c))





