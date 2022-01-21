time = input("Enter military time? ")
a = time[:2]
b = time[-2:]
h=int(a)
if h>0 and h<12:
    print(a + ":" + b + " am")
elif h==12:
    print(a + ":" + b + " pm")
elif h>12 and h<=24:
    print(str(h-12) + ":" + b + " pm")