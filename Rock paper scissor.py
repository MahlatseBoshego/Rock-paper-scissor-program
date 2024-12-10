import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissor']
print('                                                                          Welcome to the Rock,Paper and Scissors game.')
user_name = input('Enter your name: ')
print(f'Hello', user_name+'!')
print('Here are the rules:')
print('Rock beats scissor, scissor beat paper, and paper beats rock.')


while True:
    user_input = input('Please pick between Rock, Paper,Scissor or Q to quit: ').lower()
    if user_input == 'q':
        print('Goodbye!:)')
        quit()

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print('Computer picked', computer_pick + '.')

    if user_input == 'rock' and computer_pick == 'scissor':
        print('You won!')
        user_wins += 1

    elif user_input == 'scissor' and computer_pick == 'paper':
          print('You won!')
          user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
          print('You won!')
          user_wins += 1

    elif user_input == 'paper' and computer_pick == 'paper':
          print('Its a draw!')


    elif user_input == 'rock' and computer_pick == 'rock':
          print('Its a draw!')


    elif user_input == 'scissor' and computer_pick == 'scissor':
          print('Its a draw!')


    else:
        print("Your lost!")
        computer_wins +=1

print("You won", user_wins, "times.")
print('The computer won', computer_wins, "times.")
print('Goodbye!')
