'''This module contains a couple of games functions'''

# rock-paper-scessor game
import random
def rock_paper_scissor():
    '''This function takes two inputs from player and computer
    and returns the result of rock-paper-scissor game'''
    pc_choise = ['rock', 'paper', 'scissor']
    while True:
        pc = pc_choise[random.randint(0, 2)]
        user = input("Enter your choise (rock/paper/scissor) or 'q' to quit: ").lower()
        if user == 'q':
            print("Thanks for playing!")
            break
        elif pc == user:
            print(f"Both players selected {user}. It's a tie!")
        elif (pc == 'rock' and user == 'scissor') or (pc == 'scissor' and user == 'paper') or (pc == 'paper' and user == 'rock'):
            print(f"You chose {user}, computer chose {pc}. You lose!")
        elif (user == 'rock' and pc == 'scissor') or (user == 'scissor' and pc == 'paper') or (user == 'paper' and pc == 'rock'):
            print(f"You chose {user}, computer chose {pc}. You win!")
        else:
            print("Invalid input. Please try again.")