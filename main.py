# Importing Random
import random


# Welcome message
user_level = int(input('***** Choose Level *****\n'
                       'Level 1. Easy(1-20)\n'
                       'Level 2. Medium(1-250)\n'
                       'Level 3. Difficult(1-500)\n\n'
                       'Enter prefered level: '))

print(f'Level {user_level}')

# Level container
level = 0

if user_level == 1:
    level = 25
elif user_level == 2:
    level = 250
elif user_level == 3:
    level = 500
else:
    print('Invalid Level Selection')
    exit(1)

guess = random.randint(1, level)
chances = 1
i = 0
while i < 5:
    # user's input
    user_input = int(input(f'Enter a number between 1 - {level}: '))
    if user_input == guess:
        print(f'You won using {chances}')
        break
    else:
        if user_input > guess:
            print(f'Too high, Try Again!!!')
        else:
            print(f'Too low, Try Again')
    i += 1
print('Program Ended!!!')
