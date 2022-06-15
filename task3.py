from re import X


word=input('enter word:')
print(f'you entered: {word} and its type is {type(word)}')

x=list(word)
for i in x[0::2]:
     print(i)