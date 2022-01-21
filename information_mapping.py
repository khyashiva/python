"""
Q4. Information mapping using dictionary
dna : A, T, C, G
      |  |  |  |
rna : U, A, G, C
I/P: ATTCGATTCGGTGCTGATGCTGTGATGCTGATTCTCGTTCGTATGCT (dna)
O/P: UAAGC... (rna)
"""

l1 = ['A','T','C','G']
l2 = ['U','A','G','C']

d = dict(zip(l1,l2))
print(d)

dna = input("? ")
rna = ""

for i in dna:
    rna += d.get(i)

print(rna)


























