"""
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET =1

COL=3
ROWS =3

def deposit():
    while True:
        amount_str = input("How much would you like to deposit? $")
        if amount_str.isdigit():
            amount = int(amount_str)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount

def get_number_of_lines():
    while True:
        lines_str = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines_str.isdigit():
            lines = int(lines_str)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines (1-" + str(MAX_LINES) + ").")
        else:
            print("Please enter a valid number.")

    return lines

def bet(deposited_amount, selected_lines):
    bet_amount = 0
    while True:
        bet_str = input("How much would you like to bet on each line? $")
        if bet_str.isdigit():
            bet_amount = int(bet_str)
            if MIN_BET <= bet_amount <= MAX_BET and 0 < bet_amount <= deposited_amount:   #bet() function checks that the bet amount entered is within the specified range (MIN_BET to MAX_BET) and less than or equal to the deposited amount.
                break
            else:
                print(f"Bet amount must be between {MIN_BET} and {MAX_BET} and less than or equal to your deposited amount.")
        else:
            print("Please enter a valid number.")

    total_bet = bet_amount * selected_lines
    return total_bet
    
bet() function, which takes the deposited amount and the selected lines as arguments and 
returns the total bet amount. It prompts the user to enter the bet amount for each line and ensures that the bet amount is valid.

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")





# Example usage:
deposited_amount = deposit()
selected_lines = get_number_of_lines()
total_bet_amount = bet(deposited_amount, selected_lines)

print("Deposited amount:", deposited_amount)
print("Selected lines:", selected_lines)
print("Total bet amount:", total_bet_amount)



import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COL = 3
ROWS = 3

def deposit():
    while True:
        amount_str = input("How much would you like to deposit? $")
        if amount_str.isdigit():
            amount = int(amount_str)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount

def get_number_of_lines():
    while True:
        lines_str = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines_str.isdigit():
            lines = int(lines_str)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines (1-" + str(MAX_LINES) + ").")
        else:
            print("Please enter a valid number.")

    return lines

def bet(deposited_amount, selected_lines):
    bet_amount = 0
    while True:
        bet_str = input("How much would you like to bet on each line? $")
        if bet_str.isdigit():
            bet_amount = int(bet_str)
            if MIN_BET <= bet_amount <= MAX_BET and 0 < bet_amount <= deposited_amount:
                break
            else:
                print(f"Bet amount must be between {MIN_BET} and {MAX_BET} and less than or equal to your deposited amount.")
        else:
            print("Please enter a valid number.")

    total_bet = bet_amount * selected_lines
    return total_bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        total_bet = bet(balance, lines)

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${total_bet // lines} on each line. Total bet is equal to: ${total_bet}")

# Example usage:
deposited_amount = deposit()
selected_lines = get_number_of_lines()
spin(deposited_amount)

"""