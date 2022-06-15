
def remove_chars(word, num):
    print('Original string:', word)
    a=word[num:]
    return a
word = input('enter a word:')
num = input('enter a number of character to remove:')
num=int(num)
print(remove_chars(word, num))