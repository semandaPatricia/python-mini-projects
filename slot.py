import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COL = 3
ROWS = 3

SYMBOLS = ["cherry", "lemon", "orange", "plum", "bell", "bar"]

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

def spin_reels():
    return [random.choice(SYMBOLS) for _ in range(COL)]

def determine_outcome(reels):
    # Implement logic to determine the outcome based on the combination of symbols
    # For simplicity, let's say any three matching symbols result in a win.
    if len(set(reels)) == 1:
        return "win"
    else:
        return "lose"

def update_balance(balance, bet_amount, outcome):
    # Implement logic to update the balance based on the outcome
    # For simplicity, let's say winning doubles the bet amount.
    if outcome == "win":
        balance += bet_amount * 2
    else:
        balance -= bet_amount
    return balance

def play_slot_machine(balance):
    while True:
        spin_result = spin_reels()
        print("Reels:", spin_result)

        outcome = determine_outcome(spin_result)
        balance = update_balance(balance, total_bet_amount, outcome)

        print("Outcome:", outcome)
        print("New balance:", balance)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Example usage:
deposited_amount = deposit()
selected_lines = get_number_of_lines()
total_bet_amount = bet(deposited_amount, selected_lines)

print("Deposited amount:", deposited_amount)
print("Selected lines:", selected_lines)
print("Total bet amount:", total_bet_amount)

play_slot_machine(deposited_amount)
