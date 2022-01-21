#6. Write a program count the number of consonants in the word "Aeroplane".

print("enter the sentence:")
sentence = input("?")
vowels = "aeiou"
count = 0

for i in sentence:
    if i.lower() not in vowels:
        count += 1
print(count)


