
def display_list(lst):
    for item in lst:
        print(str(item), end=" ")
    print()  # for newline

def list_demo():
    fruits = ["apple", "banana", "cherry"] # list of strings
    display_list(fruits)

    empty_list = [] # empty list
    mixed_list = [1, "two", 3.0, True] # list with mixed data types

    display_list(mixed_list)

    # operations
    fruits.append("date") # add an item
    display_list(fruits)

    fruits.remove("banana") # remove an item
    display_list(fruits)

    del fruits[0] # delete item at index 0
    display_list(fruits)

    # check if item exists
    if "cherry" in fruits:
        print("Cherry is in the list fruits.") 
    else:
        print("cherry is not in the list fruits.")

def total_lunch_expense():
    lunch_expenses = [12.50, 15.00, 9.75, 20.00] # list of lunch expenses
    total = sum(lunch_expenses)
    print(f"Total lunch expense: ${total:.2f}")
    # other way of print 
    print("Total lunch expense: $", total) # print will add a space automatically

    # if we don't want print to add space, we can specify the separator parameter
    print("Total lunch expense: $", total, sep="") 

def loop_using_range():
    print("Looping using range:")
    for i in range(5): # 0 to 4
        print(i, end=" ")
    print()

def loan_payment_calculator():
    # Get details of load
    money_owed = float(input("Enter the amount of money owed in dollars: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): "))
    payment = float(input("Enter the monthly payment amount in dollars: "))
    months = int(input("Enter the number of months to simulate: "))

    interest_rate_per_month = annual_interest_rate / 100 / 12
    for month in range(1, months + 1):
        interest = money_owed * interest_rate_per_month
        money_owed += interest
        money_owed -= payment
        if money_owed < 0:
            money_owed = 0
        print(f"After month {month}, remaining balance: ${money_owed:.2f}")
        if money_owed == 0:
            print("Loan fully paid off!")
            break


if __name__ == "__main__":
    loan_payment_calculator()