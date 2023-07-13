# Importing Random
import random


guess = random.randint(1, 20)
i = 0
chances = 0
while i < 5:
    # user's import
    user_input = int(input('Enter a number 1 - 20: '))
    if user_input == guess:
        print(f'You won using {chances}')
        break
    else:
        if user_input > guess:
            print('Too high, Try Again!!!')
        else:
            print('Too low, Try Again')
    i += 1
print('Program Ended!!!')
