#### WAP to check if a given word has consecutive vowels.

word = input("enter the word:")

def isconsecutive(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1] and word[i].lower() in 'aeiou':
            return True
    return False

print(isconsecutive(word))

