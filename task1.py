number1 = input("Please enter first number:")
number1= int(number1)
print(f'You entered {number1} and its type is {type(number1)}')

number2 = input("Please enter second number:")
number2=int(number2)
print(f'You entered {number2} and its type is {type(number2)}')

product=number1*number2
if product<=1000:
    print(product)
else:
    print(number1+number2)
20