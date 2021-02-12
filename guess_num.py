import random

while True:
    upper = int(input('Please enter upper limit number:'))
    lower = int(input('Please enter lower limit number:'))
    if upper <= lower:
        print('Please enter valid range')
    else:
        break

upper_range = upper
lower_range = lower
answer = random.randint(lower, upper)

while True:
    guess = int(input('Guess number:'))
    if guess == answer:
        print('Congradulation!!')
        break
    elif guess < answer:
        lower_range = guess
        print('The answer is within ', lower_range, 'and ', upper_range)
    else:
        upper_range = guess
        print('The answer is within ', lower_range, 'and ', upper_range)