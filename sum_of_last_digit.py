"""
 WAP to find the sum of last digits in a given list of numbers.
[23, 45, 500, 6001] --> 9
Hint: 3+5+0+1
"""

numbers = eval(input("enter the numbers:"))

var = 0
for i in numbers:
    var += i % 10

print(var)
