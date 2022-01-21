#WAP to filter all the names from a list of names that begins with vowels

names = eval(input("enter the list:"))
vowels = 'aeiou'
var = []
for i in names:
    if i[0].lower() in vowels:
        var.append(i)
print(var)

