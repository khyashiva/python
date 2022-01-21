"""

13. WAP to find the number of occurances of digit in book page numbers.
Example:

    Book size: 11 , i.e, page numbers are [1, 2, 3, 4, 5, 6, 7, 8,  10, 11]
    Digit to find: 1

    Output: 4 for number of occurances of 1 in [1, 10, 11]
"""

size = eval(input("enter book size> "))
l = []
for i in range(1,size+1):
    l.append(i)
print(l)

f = eval(input("enter digit to find:"))
count = 0
for i in l:
    while i > 0:
        if i%10 == 1:
            count += 1
        i = i // 10

print(count)


