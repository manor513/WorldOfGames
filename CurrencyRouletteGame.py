from random import *
from currency_converter import CurrencyConverter
import Score


def get_exchange_rate():
    c = CurrencyConverter()
    i = c.convert(1, 'USD', 'ILS')
    return i


def get_guess_from_user(random_number):
    while True:
        amount = (input(f'Guess how much {random_number} USD is in ILS: '))
        if amount.isnumeric() and amount.isdecimal():
            return int(amount)
        else:
            print('invalid input, please try again')


def play(difficulty):
    diff_value = [5, 4, 3, 2, 1]
    random_number = randint(1, 100)
    exchange_rate = get_exchange_rate()
    print(f'exchange rate is {exchange_rate}')
    amount = get_guess_from_user(random_number)
    converted_amount = random_number * exchange_rate
    print(f'{random_number} converted to ILS is {converted_amount}')
    if converted_amount - diff_value[difficulty - 1] <= amount <= converted_amount + diff_value[difficulty - 1]:
        print('You won!')
        Score.add_score()
    else:
        print('You lost!')

