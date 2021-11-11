from player import Player
import random

input_name = input("Please enter your name: ")

def player_choice():
    choice = input("Please choose Rock, Paper or Scissors: ")
    return choice

def create_player(name, choice):
    new_player = Player(name, choice)
    return new_player

def create_computer_player():
    moves = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(moves)
    computer = Player("Computer", computer_choice)
    return computer

def get_winner(player, computer):
    win_lookup = {
        "scissors" : "paper",
        "rock" : "scissors",
        "paper" : "rock"
    }

    if win_lookup[player.choice.lower()] == computer.choice.lower():
        winner = player
    elif win_lookup[computer.choice.lower()] == player.choice.lower():
        winner = computer 
    else: 
        winner = None 
    
    return winner 

player_choice = player_choice()
player = create_player(input_name, player_choice)
computer = create_computer_player()
winner = get_winner(player, computer)

if winner == None: 
    print("It's a draw")
else: 
    print(f"{winner.name} won by playing {winner.choice}")
