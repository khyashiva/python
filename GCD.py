def GCD(a,b):
    if a > b:
        l = a
        s = b
    else:
        l = b
        s = a
    while(l > 0):
        r = l % s
        if(r == 0):
            print("GCD is",s)
            break
        l = s
        s = r
    return s
a,b = eval(input("a:")),eval(input("b:"))

LCM = (a*b) / GCD(a,b)
print(LCM)

# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = 54
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))

# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

# Python program to find the L.C.M. of two input number

# This function computes GCD
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

# Function to find HCF the Using Euclidian algorithm
"""
For example, if we want to find the H.C.F. of 54 and 24, we divide 54 by 24. The remainder is 6.
Now, we divide 24 by 6 and the remainder is 0. Hence, 6 is the required H.C.F.
"""

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)









