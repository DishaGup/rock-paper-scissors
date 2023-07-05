import random

def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_result(user_choice, computer_choice)
    return {
        "computer_choice": computer_choice,
        "result": result,
    }

def determine_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"
    return result

if __name__ == "__main__":
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    game_result = play_game(user_choice)
    print(game_result)
