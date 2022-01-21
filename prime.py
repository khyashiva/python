number = eval(input("enter the number"))

for i in range(2,number):
    if number % i == 0:
        print("not prime")
        break
else:
    print("prime")

number = eval(input("enter the number"))
for i in range(2,number):
    for j in range(2,i):
        if i % j == 0:
            print(str(i) +" is not prime")
            break
    else:
        print(str(i) + " is prime")