"""
### WAP to check if a given word has consecutive vowels.
True/False

school --> True
steal --> False  (True)
hello --> False
apple --> False

for i in range(len(iterable)): ...
"""

word = input("? ")
vowels = "aeiou"

for i in range(len(word) - 1):
    if word[i] == word[i +1] and word[i].lower() in "aeiou":
        print("true")
        break
else:
    print("False")


def isconsecutive(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1] and word[i].lower() in "aeiou":
        # if word[i] in "aeiou" and word[i+1] in "aeiou"
            return True
    return False

print(isconsecutive(word))





