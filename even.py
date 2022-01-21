#WAP to filter even numbers from a list of numbers.

numbers = eval(input("enter the numbers?"))
new = []
for i in numbers:
    if i % 2 == 0:
        new.append(i)

print(new)

