def calculate():
    operation = input('''
Please type the math operation would you like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = float(input(' Please enter the first number: '))
    number_2 = float(input(' Please enter the second number:'))
    if operation == '+':
       print ('{} + {} = '.format(number_1, number_2))
       print (number_1 + number_2)

    elif operation == '-':
       print('{} - {} = '.format(number_1, number_2))
       print(number_1 - number_2)

    elif operation == '*':
       print('{} * {} = '.format(number_1, number_2))
       print(number_1 * number_2)

    elif operation == '/':
       print('{} / {} = '.format(number_1, number_2))
       print(number_1 / number_2)

    else:
      print ('You have entered a wrong statement!')
    again()

def again():
    calculation_again = input('''
    Do you want to calculate again?
    Type Y for yes or N for no
    ''')
    if calculation_again.upper() == 'Y':
        calculate()
    elif calculation_again.upper() == 'N':
        print('Bye, Thank you, come again')
    else:
        again()

calculate()





