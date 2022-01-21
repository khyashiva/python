# WAP to find the number of occurances for the list word ['a', 'an', 'the'] in below paragraph

sentence = input("enter the sentence:")
p = sentence.split()

for i in ['a','an','the']:
    print(i,p.count(i))



