import random
import Score


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        print('Guess a number between 1 and ' + str(difficulty))
        user_guess = (input())
        if user_guess.isnumeric() and user_guess.isdecimal():
            user_guess = int(user_guess)
            if user_guess >= 1 and user_guess <= difficulty:
                break
            else:
                print('Invalid input, please try again')
        else:
            print('invalid input, please try again')
    return user_guess


def compare_results(guess, secret_number):
    if guess == secret_number:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if compare_results(guess, secret_number) is True:
        print('You won!')
        Score.add_score()
    else:
        print('You lost!')
    print('secret number: ', secret_number)


