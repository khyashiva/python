#WAP to reverse a dictionary with diplaicate values without information loss.

d = {1: 'a', 2:'b', 3:'c', 4:'b'}
#reverse a string
r = {v:k for k, v in d.items()}
#{'a': 1, 'b': 4, 'c': 3}

s = {v:[k] for k, v in d.items()}
#{'a': [1], 'b': [4], 'c': [3]}

k = {v:[i for i in d.keys()] for k, v in d.items()}
#{'a': [1, 2, 3, 4], 'b': [1, 2, 3, 4], 'c': [1, 2, 3, 4]}

answer = {v:[i for i in d.keys() if d[i]==v] for k, v in d.items()}
#{'a': [1], 'b': [2, 4], 'c': [3]}
