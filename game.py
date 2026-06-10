## ROCK PAPER SCISSOR GAME
import random

entity = ["rock", "paper", "scissor"]
VALID_CHOICES = set(entity)


def play_round(user_choice: str) -> dict:
    user = user_choice.lower().strip()

    if user not in VALID_CHOICES:
        return {
            "outcome": "invalid",
            "user": user,
            "pc": None,
            "message": "Please choose rock, paper, or scissor.",
        }

    pc = random.choice(entity)

    if user == pc:
        outcome = "tie"
        message = f"It's a tie! You both chose {user}."
    elif (
        (user == "rock" and pc == "scissor")
        or (user == "scissor" and pc == "paper")
        or (user == "paper" and pc == "rock")
    ):
        outcome = "win"
        message = f"You won! {user.capitalize()} beats {pc}."
    else:
        outcome = "lose"
        message = f"You lost! {pc.capitalize()} beats {user}."

    return {
        "outcome": outcome,
        "user": user,
        "pc": pc,
        "message": message,
    }


if __name__ == "__main__":
    print("Rock Paper Scissors")
    print("Type q at any prompt to quit.\n")

    while True:
        print("--- New Round ---")
        user = input("Rock, paper, or scissor: ")

        if user.lower().strip() == "q":
            print("Thanks for playing!")
            break

        result = play_round(user)
        print(result["message"])

        if result["outcome"] == "invalid":
            continue

        input("\nPress Enter to continue...")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
