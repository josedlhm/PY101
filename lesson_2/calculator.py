print('Welcome to Calculator!')

print("What's the first number?")
number1 = input()

print("What's the second number?")
number2 = input()

print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':   # '1' represents addition
    output = int(number1) + int(number2)
elif operation == '2':
    output = int(number1) + int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
    output = int(number1) / int(number2)

print(f"The result is: {output}")
