import random

# Asks the user for amount of numbers they want with error handling
def get_amount_of_numbers():
    while True:
        try:
            amount = int(input("How many numbers would you like in the equation? (minimum 2)"))
            if amount < 2:
                print("You need at least 2 numbers for the equation.")
            else:
                return amount
        except:
            print("Please enter an integer.")

# Picks a random operator: +, -, or *
def operation():
    operator_list = list('+-*')
    return random.choice(operator_list)

# Main function that generates and solves the math problem
def main(amount_of_numbers):
    numbers = [random.randint(2, 10) for numbers in range(amount_of_numbers)]
    symbol = operation()

    # Calculates the correct answer based on the chosen operator
    if symbol == '+':
        answer = sum(numbers)
    elif symbol == '-':
        answer = numbers[0]
        for number in numbers[1:]:
            answer -= number
    elif symbol == '*':
        answer = 1
        for number in numbers:
            answer *= number

    # Asks the user for the answer with error handling
    while True:
        user_input = input(f"What is {f' {symbol} '.join(map(str, numbers))}? ")

        try:
            user_input = int(user_input)
        except:
            print("Enter an integer‼")
            continue

        if user_input == answer:
            print("Good Boy!")
            break
        else:
            print("Bad Boy!!")
            print(f"Correct answer was {answer}")
            break

amount = get_amount_of_numbers()
main(amount)
