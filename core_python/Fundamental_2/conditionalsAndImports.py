
import datetime, random

# <, <=, >, >=, ==, != comparison operators
# or and not logical operators. Or and or let you combine multiple conditions while not negates a condition.
# True or False boolean values

def condition_demo(temperature: float):
    if temperature < 0:
        return "It's freezing!"
    elif 0 <= temperature < 20:
        return "It's cold."
    elif 20 <= temperature < 30:
        return "It's warm."
    elif temperature >= 80:
        return "It's too hot. Stay indoors."
    else:
        return "It's hot!"

def rock_paper_scissors():
    # give the below random function a seed that is current date time oa value
    random.seed(int(datetime.datetime.now().timestamp()))
    computer_choice = random.choice(["rock", "paper", "scissors"])
    user_chose = input("Enter rock, paper, or scissors: ").lower()

    if computer_choice == user_chose:
        print("TIE")
    elif (user_chose == "rock" and computer_choice == "scissors") or \
         (user_chose == "scissors" and computer_choice == "paper") or \
         (user_chose == "paper" and computer_choice == "rock"):
        print("YOU WIN")
    else:
        print("YOU LOSE")
    print(f"Computer chose: {computer_choice}")

if __name__ == "__main__":
    rock_paper_scissors()