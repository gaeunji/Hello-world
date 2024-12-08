import random

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "Win"
    else:
        return "Lose"

def play_again(input_choice):
    if input_choice == "no":
        return False
    return True

# 게임 시작
if __name__ == "__main__":
    while True:
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)

        player = ''
        while player not in choices:
            player = input("rock, paper, or scissors?: ").lower()

        result = determine_winner(player, computer)
        print(f"Computer: {computer}")
        print(f"You: {player}")
        print(result + "!")

        # 재시작 여부
        play_again_choice = ''
        while play_again_choice not in ["yes", "no"]:
            play_again_choice = input("Play again? (yes/no): ").lower()

        if not play_again(play_again_choice):
            print("Bye!")
            break
