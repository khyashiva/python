
s1 = input("> ")
s2 = input("> ")

s3 = sorted(list(s1.lower()))
s4 = sorted(list(s2.lower()))

if s3 == s4:
    print("anagram")
else:
    print("Not an anagram")




