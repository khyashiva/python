"""
8. Write a program to remove duplicate letters from a given word (case-insensitive).
    Example1: 'foosball' --> 'fosbal'
    Example2: 'Aeroplane' --> 'Aeropln'
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