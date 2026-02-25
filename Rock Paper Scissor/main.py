import random

def user():
    print("\nChoose one:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    choice = input("Enter your choice: ")

    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    elif choice == "3":
        return "scissors"
    else:
        return None

def computer():
    return random.choice(["rock", "paper", "scissors"])

def winner(user, computer):
    if user == computer:
        return "tie"
    elif user == "rock" and computer == "scissors":
        return "user"
    elif user == "paper" and computer == "rock":
        return "user"
    elif user == "scissors" and computer == "paper":
        return "user"
    else:
        return "computer"

print("Welcome to Rock Paper Scissors 😊")
print("Game created by Utsav Kumar Jha")

user_score = 0
computer_score = 0

while True:
    user_choice = user()

    if user_choice == None:
        print("Invalid input, please try again.")
        continue

    computer_choice = computer()

    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    result = winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round 🎉")
        user_score += 1
    else:
        print("Computer wins this round 💻")
        computer_score += 1

    print("Score → You:", user_score, "| Computer:", computer_score)

    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again != "y":
        print("\nThanks for playing!")
        print("Made by Utsav Kumar Jha ❤️")
        break