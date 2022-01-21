"""

10. Write a program to count the number of names beginning with vowels in a given tuple of names.
    >>> ['Apple', 'Google', 'iGate', 'devU', '3M', 'Oracle']
    3
"""

l = eval(input("? "))

vowels = "aeiou"
count = 0
for i in l:
    if i[0].lower() in vowels:
        count += 1

print(count)

