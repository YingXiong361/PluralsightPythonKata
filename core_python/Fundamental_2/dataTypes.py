

def data_types_demo():
    # print function
    print("Hello, World!")


    # primitive data types
    amount = int(10.5) # integer
    print(f"amount: {amount}, type: {type(amount)}")
    amount2 = float(10) # float
    print(f"amount2: {amount2}, type: {type(amount2)}")
    name = 'John Doe' # text
    print(name)
    name2 = "John's Doe" # text
    print(name2)

    # input function
    name = input("what's your name? \n")  
    print("Hello " + " " + name)

def decades():
    birth_year = int(input("Enter your birth ages: \n"))
    decade = (birth_year // 10) * 10
    years = birth_year % 10
    print(f"You were born in the {decade}s and {years} years old.")

if __name__ == "__main__":
    data_types_demo()
    decades()