#armstrong
#153 = 1 * 3 + 5 * 3 + 3 * 3
n = input("enter the number:")
def armstrong(n):
    l = list(n)
    print(l)
    c = len(l)
    print(c)
    sum = 0
    for i in l:
        sum = sum + int(i) ** c
    return sum

sum = armstrong(n)

if sum == int(n):
    print("armstrong number")
else:
    print("not an armstrong")


# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
