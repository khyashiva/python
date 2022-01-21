#Q5. WAP to reverse a dictionary with diplaicate values without information loss.

d = {1: 'a', 2:'b', 3:'c', 4:'b'}

#reverse a dictonary

c = {v:k for k,v in d.items()}
print(c)

e = {v:[k] for k,v in d.items()}
print(e)

f = {v:[i for i in d.keys()] for k,v in d.items()}
print(f)

g = {v:[i for i in d.keys() if d[i]==v] for k,v in d.items()}
print(g)




