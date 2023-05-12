num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))
operator = input('Enter a math operator to perform an action with both numbers:')

if(operator == '+'):
    print(num1 + num2)
elif (operator == '*'):
    print(num1 * num2)
elif(operator == '/'):
    print(round(num1 / num2))
elif (operator == '-'):
    print(num1 - num2)   
else: print('Oops! You have entered an invalid math operator :(')         
