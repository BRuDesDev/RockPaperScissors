import random
import player_art
import cpu_art

# handle game stats
gameStats = {
    'playerWins': 0,
    'compWins': 0,
    'ties': 0,
    'roundNum': 1,
}


def reward_winner(winner):
    # Increase winner's score by 1
    if winner == 'tie':
        gameStats['ties'] += 1
    elif winner == 'CPU':
        gameStats['compWins'] += 1
    elif winner == 'Player':
        gameStats['playerWins'] += 1
    # advance round by 1
    gameStats['roundNum'] += 1


def print_round_info():
    # Check if NEW GAME
    if gameStats['roundNum'] == 1 and gameStats['ties'] == 0 and gameStats['compWins'] == 0 and gameStats['playerWins'] == 0:
        print(player_art.game_title)
        print(f" \n--------------------------------------------")
        print(f"NEW GAME! - Player=0 ~ CPU=0 ~ Ties=0")
        print_instructions()
    else:
        print(f"Player={gameStats['playerWins']} |~| CPU={gameStats['compWins']} |~| Ties={gameStats['ties']}")


def print_instructions():
    print("To play, select your hand each round. (r)Rock (p)Paper (s)Scissors")
    print("10 rounds... BEGIN!\n\n")


def get_user_choice():
    player_hand = input("Choose your hand: (r,p,s)")
    if player_hand.lower() == 'r':
        return 1
    elif player_hand.lower() == 'p':
        return 2
    elif player_hand.lower() == 's':
        return 3
    else:
        print("Sorry your input could not be understood, try again")
        get_user_choice()


def get_computer_choice():
    comp_choice = random.randint(1, 3)
    return comp_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == 1 and computer_choice == 2:
        return "CPU"
    elif user_choice == 1 and computer_choice == 3:
        return "Player"
    elif user_choice == 2 and computer_choice == 1:
        return "Player"
    elif user_choice == 2 and computer_choice == 3:
        return "CPU"
    elif user_choice == 3 and computer_choice == 1:
        return "CPU"
    elif user_choice == 3 and computer_choice == 2:
        return "Player"


def display_result(user_choice, computer_choice, winner):
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    user_choice_str = choices[user_choice]
    computer_choice_str = choices[computer_choice]

    print(f"Player threw {user_choice_str} |~| CPU threw {computer_choice_str}")

    if winner == 'tie':
        print(f"It's a tie! \n --------------------------------")
    elif winner == 'Player':
        print(f"Player wins! \n --------------------------------")
    elif winner == 'CPU':
        print(f"CPU wins! \n --------------------------------")
    else:
        print(f"Winner didn't register... try again \n --------------------------------")
        play_game()


def play_game():
    if gameStats['roundNum'] == 1:
        print(player_art)
    print_round_info()
    comp_choice = get_computer_choice()
    player_choice = get_user_choice()
    winner = determine_winner(player_choice, comp_choice)
    display_result(player_choice, comp_choice, winner)
    reward_winner(winner)


while gameStats['roundNum'] < 10:
    play_game()

# Main program
if __name__ == "__main__":
    play_game()
