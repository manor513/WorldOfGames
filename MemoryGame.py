import random
import time
import os
import Score


def generate_sequence(difficulty):
    numbers = [random.randint(1, 101) for _ in range(difficulty)]
    print(numbers)
    time.sleep(0.7)
    os.system("cls" if os.name == "nt" else "clear")
    return numbers


def get_list_from_user():
    while True:
        user_input = input("Enter the numbers you remember separated by spaces: ")
        lst = user_input.split()
        valid = True
        for item in lst:
            if not item.isdigit():
                valid = False
                break
        if valid:
            lst = [int(i) for i in lst]
            break
        print("Invalid input. Please try again.")

    print(lst)
    return lst


def is_list_equal(numbers, user_numbers):
    if numbers == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    numbers = generate_sequence(difficulty)
    user_numbers = get_list_from_user()
    is_list_equal(numbers, user_numbers)
    if is_list_equal(numbers, user_numbers) is True:
        print('You won!')
        Score.add_score()
    else:
        print('You lost!')

