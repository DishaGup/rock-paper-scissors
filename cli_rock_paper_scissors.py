# rock_paper_scissors.py
import random

def play_game(user_choice):
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        if user_choice == computer_choice:
            print("It is a draw!")
            draws += 1
            print(f"User's choice: {user_choice}, Computer's choice: {computer_choice}")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Computer wins!")
                computer_wins += 1
                print(f"User wins: {user_wins}")
                print(f"Computer wins: {computer_wins}")
                print(f"Draws: {draws}")
            else:
                print("You win!")
                user_wins += 1
                print(f"User wins: {user_wins}")
                print(f"Computer wins: {computer_wins}")
                print(f"Draws: {draws}")
            print(f"User's choice: {user_choice}, Computer's choice: {computer_choice}")
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("Computer wins!")
                computer_wins += 1
                print(f"User wins: {user_wins}")
                print(f"Computer wins: {computer_wins}")
                print(f"Draws: {draws}")
            else:
                print("You win!")
                user_wins += 1
                print(f"User wins: {user_wins}")
                print(f"Computer wins: {computer_wins}")
                print(f"Draws: {draws}")
            print(f"User's choice: {user_choice}, Computer's choice: {computer_choice}")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins!")
                computer_wins += 1
                print(f"User wins: {user_wins}")
                print(f"Computer wins: {computer_wins}")
                print(f"Draws: {draws}")
            else:
                print("You win!")
                user_wins += 1
                print(f"User wins: {user_wins}")
                print(f"Computer wins: {computer_wins}")
                print(f"Draws: {draws}")
            print(f"User's choice: {user_choice}, Computer's choice: {computer_choice}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
