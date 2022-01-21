
l = eval(input("> "))

l.pop(0)
l.pop(-1)

print(l)

#5. Write a program to print a list of all indexes for a value in the list.

for i in l:
    print(l.index(i))

#6. Write a program to reverse key:value pair in a dictionary.

d = eval(input("> "))
print({v:k for k,v in d.items()})


