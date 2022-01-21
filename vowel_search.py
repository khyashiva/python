#WAP to check to if a given word both begins and ends with vowels.

word = input("enter the word:")
vowels = "aeiouAEIOU"

if word[0] in vowels and word[-1] in vowels:
    print(True)
else:
    print(False)

#print(True if word[0] in vowels and word[-1] in vowels else False)




