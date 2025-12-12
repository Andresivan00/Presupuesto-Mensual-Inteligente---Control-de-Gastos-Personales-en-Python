# ===================================================================
# OVERVIEW
# This program helps anyone organize their monthly money:
# - Asks for salary and actual expenses
# - Calculates how much you spend and how much is left to save
# - Provides personalized recommendations based on your habits
# - Very useful for learning financial education
# ===================================================================

"""
 ------------------------------
 Function to request integers from the user with validation
 ------------------------------
"""
def ask_number(message: str) -> int: 
    """
    Asks the user for an integer.
    If they enter letters or symbols, shows an error and asks again.
    Example: "Enter your monthly salary: "
    """
    while True:  # Repeats until the user enters a valid number
        try:
            return int(input(message))  # Converts input to a number
        except ValueError:
            print("Error: enter a valid number. Only whole numbers!")  # Clear error message

"""
 ------------------------------
 Function to validate housing type
 ------------------------------
"""
def ask_housing_type() -> str:
    """
    Asks if the housing is 'owned' or 'rented'.
    Only accepts those two words (in lowercase).
    If they enter something else, insists until they do it correctly.
    """
    while True:
        housing_type = input("Type if you have housing 'owned' or 'rented': ").lower()  # .lower() accepts uppercase
        if housing_type in ["owned", "rented"]:
            return housing_type  # Returns the valid option
        print("Invalid option. Only type: 'owned' or 'rented'.")

"""
 ------------------------------
 Function that calculates how much you spend and how much you save
 ------------------------------
"""
def calculate_budget(salary: int, housing: str, rent: int, bills: int, other: int, desired_savings: int):
    """
    Calculates:
    - expenses = everything you spend (rent + bills + food/entertainment)
    - savings = salary - expenses (what you actually have left)
    Returns both values as a tuple.
    """
    expenses = rent + bills + other  # Sums all fixed and variable expenses
    savings = salary - expenses      # What remains after paying everything
    return expenses, savings         # Returns two values

"""
 ------------------------------
 Function that shows nice results and gives advice
 ------------------------------
"""
def show_results(expenses: int, savings: int, desired_savings: int, other: int, bills: int):
    """
    Shows the financial summary and gives smart advice:
    - If you spend more on movies/food than on bills → gives a little scolding
    - If you don't reach your desired savings → motivates you to reduce small expenses
    - If you achieved it → congratulates you!
    """
    print(f"\nYour monthly expenses are: ${expenses:,}")
    print(f"Your monthly savings are: ${savings:,}")

    # Alert if you spend too much on entertainment/food
    if other >= bills:
        print("Your spending on other services is very high, you should try going to the movies less")

    # Compares your savings goal with reality
    if desired_savings > savings:
        print("You need to take measures to reach your desired savings, you can start by eliminating small unnecessary expenses.")
    else:
        print("Well done, your goals have been achieved")


"""
 ------------------------------
 Main function - This is where everything starts
 ------------------------------
"""
def main():
    """
    Main function that coordinates the entire program:
    1. Greets and asks for all data
    2. Calculates the budget
    3. Shows results with advice
    """
    print("=== PERSONAL FINANCIAL PLANNER ===")
    print("Let's see how much money you actually have left each month!\n")

    # === DATA INPUT ===
    salary = ask_number("Enter your monthly salary: $")
    housing = ask_housing_type()
    
    # If they rent, asks how much they pay. If owned → rent = 0
    rent = ask_number("Enter your rent expense: $") if housing == "rented" else 0
    
    bills = ask_number("Enter the average expenses for services (electricity, water, internet): $")
    other = ask_number("Enter the average for eating out, movies, outings, etc: $")
    desired_savings = ask_number("How much money do you want to save per month?: $")

    # === CALCULATION ===
    expenses, savings = calculate_budget(salary, housing, rent, bills, other, desired_savings)
    
    # === RESULTS ===
    show_results(expenses, savings, desired_savings, other, bills)

    print("\nThank you for using the planner! Remember: the first step to becoming rich is knowing where your money goes")


"""
 ------------------------------
 Runs the program only if executed directly
 ------------------------------
"""
if __name__ == "__main__":
    main()
