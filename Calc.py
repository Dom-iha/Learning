from ast import While

print('Thank you for choosing Pycalc')

contd = 1

while True:
    

    Num1 = float(input('Enter a number: '))
    op = input('Choose operator: ')
    Num2 = float(input('Enter a number: '))

    if op == "/":
        print(Num1 / Num2)
    elif op == "-":
        print(Num1 - Num2)
    elif op == "*":
        print(Num1 * Num2)
    elif op == "+":
        print(Num1 + Num2)
    else:
        print('INVALID OPERATOR!')

    contd = input('Continue?(0/1): ')
    
    if contd == 0:
        print('Thank you for using Pycalc')


