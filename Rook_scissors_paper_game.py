import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It' tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
    (user_choice == 'scissors' and computer_choice == 'paper') or \
    (user_choice == 'paper' and computer_choice == 'rock'):

        return "You win!"
    else:
        return "You lose"

def play_game():
    choices = ['rock' , 'paper' , 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        print("\n Welcome to Rock-paper-scissors game!")
        print("Choice your weapon: rock, paper, scissors.")
        user_choice = input("Enter your choice:").lower()

        if user_choice not in choices:
            print("Invalid choice. please choose rock, paper or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"\n Your chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(user_choice , computer_choice)
        print(result)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        print(f"\n Your score: {user_score} | Computer's score: {computer_score}")

        play_again = input("\n Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n Thank for playing!")
            break
play_game()