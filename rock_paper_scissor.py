# Python program for Rock-Paper Scissor game.
 
import random

def play():
    user_wins = 0
    computer_wins = 0
    while True:
        choices = ['rock', 'paper', 'scissor']
        user_choice = input("Enter your choice: rock, paper, or scissor: ").lower()
        computer_choice = random.choice(choices)
        
        if user_choice not in choices:
            print("Invalid Input! Try again...")
            continue
        
        print(f'User choice: {user_choice}')
        print(f'Computer choice: {computer_choice}')
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissor' and computer_choice == 'paper'):
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
        
        print(f"You have won {user_wins} times and the computer has won {computer_wins} times.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("End of the game! Thanks for playing!")
            break

play()