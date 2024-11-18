import random


def play_round():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Choose Rock, Paper, or Scissors (or 'exit' to quit): ").strip().lower()

    if user_choice == "exit":
        return None  # To signal end of the game

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return 0, 0  # No points awarded if there's an invalid choice

    print(f"Computer chose: {computer_choice}")

    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a tie!")
        return 0, 0  # No points for a tie
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        return 1, 0  # User wins this round
    else:
        print("Computer wins this round!")
        return 0, 1  # Computer wins this round


def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'exit' anytime to quit the game.")

    while True:
        # Get the result from play_round
        result = play_round()

        # Check if the user wants to exit
        if result is None:
            break

        # If not exiting, unpack the results
        user_points, computer_points = result

        # Update scores
        user_score += user_points
        computer_score += computer_points

        print(f"Score: You - {user_score}, Computer - {computer_score}\n")

    # Final result
    print("\nFinal Scores:")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations, you are the overall winner!")
    elif computer_score > user_score:
        print("Computer wins overall. Better luck next time!")
    else:
        print("It's an overall tie!")


# Start the game
play_game()