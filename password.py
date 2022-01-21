#WAP to check if a given password has at least one digit

password = input("enter the password:")
count = 0
for i in password:
    if i.isdigit():
        count += 1

print(True if count >=0 else False)



