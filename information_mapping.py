"""
 Information mapping using dictionary
dna : A, T, C, G
      |  |  |  |
rna : U, A, G, C
I/P: ATTCGATTCGGTGCTGATGCTGTGATGCTGATTCTCGTTCGTATGCT (dna)
O/P: UAAGC... (rna)

"""

dna=['A','T','C','G']
rna=['U','A','G','C']
d = dict(zip(dna, rna))
dna = input("Enter dna: ")
rna = ""
for i in dna:
    rna += d.get(i)
print(rna)

