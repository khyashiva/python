year = eval(input("enter the year"))

if year % 4 == 0 and (year%100 !=0 or year%400==0):
    print("leap year")
else:
    print("not a leap year")

year = eval(input("enter the year"))

for i in range(year):
    if i % 4 == 0 and (i % 100 !=0 or i % 400 == 0):
        print(i)
    else:
        pass

