"""
8. Write a program to remove duplicate letters from a given word (case-insensitive).
    Example1: 'foosball' --> 'fosbal'
    Example2: 'Aeroplane' --> 'Aeropln'

"""

word = input("? ")
word2 = ""

for i in word:
    if i not in word2:
        word2 = word2 + i
print(word2)

