#WAP to count the number of vowels in a given word.

word = input("enter the word:")
count = 0
for i in word:
    if i.lower() in 'aeiou':
        count += 1
print(count)



