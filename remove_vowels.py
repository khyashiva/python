word = input("enter the word:")
vowels = "aeiou"
new = ""
for i in word:
    if i.lower() not in vowels:
        new += i

print(new)


