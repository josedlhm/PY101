def prompt(message):
    print(f'==> {message}')
    
prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

prompt("What's the second number?")
number2 = input()

prompt('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

match operation:
    case '1':   # '1' represents addition
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) + int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

prompt(f"The result is: {output}")
