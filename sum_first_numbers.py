#WAP to find the sum of first digits from a given list of numbers

numbers = eval(input("enter the list of numbers:"))
total = 0
for i in numbers:
    total  += int(str(i)[0])

print(total)
