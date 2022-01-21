"""
LabelEncoding
I/P: ['Yes', 'YES', 'No', 'yes', 'no', '']
O/P: [1, 1, 0, 1, 0, 1]
"""

l1 = eval(input("L1> "))
l2 = []

for i in l1:
    if i.lower() == 'yes':
        l2.append(1)
    elif i.lower() == 'no':
        l2.append(0)
    else:
        l2.append(1)

print(l2)

#[1 if i.lower()=="yes" else 0 for i in data]

"""
list

CURD
C-->APPEND,EXTEND,COPY,INSERT
U-->SORT,REVERSE
R-->COUNT,INDEX
D--->POP,REMOVE,del,

LIST COMPREHENSION
-->[FOR LOOP]
-->[FOR LOOP IF CONDITION]
-->[IF ELSE FOR LOOP]

DICTIONARY COMPREHENSION
{i:words.count(i) for i in words} # dictionary comprehension

"""


