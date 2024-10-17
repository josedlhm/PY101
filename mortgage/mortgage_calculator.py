import json


# Open the JSON file for reading
with open('file.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f"==> {message}")
    
def messages(message, lang='English'):
    return data[lang][message]

def invalid_number(number_str):
    try:
        float(number_str)
        if float(number_str) <= 0:
            raise ValueError(f"Value must be > 0")
    except ValueError:
        return True

    return False

def great_than_zero(number_str):
    try:
        float(number_str)>0
    except ValueError:
        return True

    return False


prompt(messages('welcome','Spanish'))

while True: 

    prompt("What's the loan amount in dollars?")
    loan_amount = input()

    while invalid_number(loan_amount):
        prompt("Hmm... that doesn't look like a valid number.")
        loan_amount = input()

    prompt("What's the Annual Payment Rate?")
    annual_payment_rate = input()

    while invalid_number(annual_payment_rate):
        prompt("Hmm... that doesn't look like a valid number.")
        annual_payment_rate = input()

    prompt("What's the duration of the loan in years?")
    loan_in_years = input()

    while invalid_number(loan_in_years):
        prompt("Hmm... that doesn't look like a valid number.")
        loan_in_years = input()

    loan_in_months = 12.0 * float(loan_in_years)

    monthly_payment_rate = (float(annual_payment_rate) / 100.0) / 12.0

    monthly_payment = float(loan_amount) * (monthly_payment_rate / (1 - (1 + monthly_payment_rate) ** (-float(loan_in_months))))

    monthly_payment = round(monthly_payment,2)

    prompt(f"The result is ${monthly_payment}")

    prompt("Would you like to perform another calculation? Answer yes or no.")
    response = input()
    if response.lower() == 'no':
        break
        
