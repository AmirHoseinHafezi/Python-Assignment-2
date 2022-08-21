import math
CN = int(input('How much do you want to use the calculator: '))
calc_type = input('what type do you want to use(Basic or Advanced): ')
if calc_type == 'Basic':
 while True:
     print("Welcome My User !!!")
     print("Enter 'add' to add two numbers")
     # Subtract Numbers
     print("Enter 'subtract' to subtract two numbers")
     # Multiply Numbers
     print("Enter 'multiply' to multiply two numbers")
     # Divide Numbers
     print("Enter 'divide' to divide two numbers")
     # Quiting Program
     print("Enter 'quit' to end the program")
     user_input = input("write: ")
     if user_input == "quit":
          print("exit")
          break
     elif user_input == "add":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 + num2)
          print("the answer >>> "+ result)
     elif user_input == "subtract":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 - num2)
          print("the answer >>> "+ result)
     elif user_input == "multiply":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 * num2)
          print("the answer >>> "+ result)
     elif user_input == "divide":
          num1 = float(input("enter first number >> "))
          num2 = float(input("enter second number >> "))
          result = str(num1 / num2)
          print("the answer >>> "+ result)
     else:
          print("unkhown input")

if calc_type == 'Advanced':
     i = 0
     while True:
               op = input(
                    '\nEnter the operator from this List\n// or correctdivision, mod or remaining\n ^2 or power2, ^ or power\n | or absolutevalue, sin, cos, tan, cot\n √ or squareroot, primenumber: ')
               num1 = float(input('Enter number: '))
               if op == '^2' or op == 'power2' or op == '|' or op == 'absolutevalue' or op == 'sin' or op == 'cos' or op == 'tan' or op == 'cot' or op == '√' or op == 'squareroot' or op == 'primenumber':
                    if op == '^2' or op == 'power2':
                         power_2 = math.pow(num1, 2)
                         print('\n', num1, 'to power of 2: ', power_2)
                    elif op == '|' or op == 'absolutevalue':
                         av = math.fabs(num1)
                         print('\nabsolute value of', num1, ': ', av)
                    elif op == 'sin':
                         sin = math.sin(num1)
                         print('\nsine of', num1, ':', sin)
                    elif op == 'cos':
                         cos = math.cos(num1)
                         print('\ncosine of', num1, ':', cos)
                    elif op == 'tan':
                         tan = math.tan(num1)
                         print('\ntangent of', num1, ':', tan)
                    elif op == 'cot':
                         cot = math.atan(num1)
                         print('\ntangent of', num1, ':', cot)
                    elif op == '√' or op == 'squareroot':
                         sr = math.sqrt(num1)
                         print('\nsquare root of', num1, ':', sr)
                    elif op == 'prime number':
                         p_cn = 0
                         for i in range(num1):
                              if num1 % i == 0:
                                   CN += 1
                         if CN == 2:
                              print('\n', num1, 'is a prime number')
                         else:
                              print('\n', num1, 'is not a prime number')
               elif op == '//' or op == 'correctdivision' or op == 'mod' or op == 'remaining' or op == '^' or op == 'power':
                    num2 = float(input('Enter number: '))
                    if op == '//' or op == 'correctdivision':
                         if num2 == 0:
                              print('\na number cannot be divided by zero')
                              continue
                         else:
                              cd = num1 // num2
                              print('\ncorrect division of', num1, 'by', num2, ': ', cd)
                    elif op == 'mod' or op == 'remaining':
                         if num2 == 0:
                              print('\na number cannot be divided by zero')
                              continue
                         else:
                              mod = num1 % num2
                              print('\nramaining of', num1, 'by', num2, ': ', mod)
                    elif op == '^' or op == 'power':
                         pow = math.pow(num1, num2)
                         print('\n', num1, 'to power of', num2, ':', pow)
               else:
                    print('\nyour operator is not supported')
                    continue
               print('\nyou used the calculator', i + 1)
