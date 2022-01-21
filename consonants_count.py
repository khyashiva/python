#6. Write a program count the number of consonants in the word "Aeroplane"

word = input("> ")
vowels = "aeiou"

count = 0

for i in word:
    if i.lower() not in vowels:
        count +=1

print(count)

"""
8. Write a program to remove duplicate letters from a given word (case-insensitive).
    Example1: 'foosball' --> 'fosbal'
    Example2: 'Aeroplane' --> 'Aeropln'
"""
"""
word = input(">")
word2 = word.lower()
word3 = "".join(list(set(list(word))))
print(word3)

"""

word = input(">")
word2 =""

#Aeroplane
#aeroplAne

for i in word:
    if i.lower() in word2 or i.upper() in word2:
        pass
    else:
        word2 += i
print(word2)

#Aeroplane
#aeroplAne
"""
if i.lower() in word2 or i.upper() in word2:
    pass
else:
    word2 += i
"""