import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome():
    name = input('Please enter your name: ')
    print(f'''Hello {name} and welcome to the World of Games (WoG)
Here you can find many cool games to play.''')


def load_game():
    while True:
        print('''Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')
        game_choose = (input())

        if game_choose.isnumeric() and game_choose.isdecimal():
            game_choose = int(game_choose)
            if game_choose >= 1 and game_choose <= 3:
                break
            else:
                print('Invalid input, Please enter a number between 1 and 3.')

        else:
            print('Invalid input, Please enter a full number between 1 and 3.')

    while True:
            difficulty = (input('Please choose a game difficulty between 1-5: '))
            if difficulty.isnumeric() and difficulty.isdecimal():
                difficulty = int(difficulty)
                if difficulty >= 1 and difficulty <= 5:
                    break
                else:
                    print('Invalid input, Please enter a number between 1 and 5.')
            else:
                print('Invalid input, Please enter a full number between 1 and 5.')

    if game_choose == 1:
        print('You chose to play the Memory Game!')
        MemoryGame.play(difficulty)

    if game_choose == 2:
        print('You chose to play the Guess Game!')
        GuessGame.play(difficulty)

    if game_choose == 3:
        print('You chose to play the Currency Roulette!')
        CurrencyRouletteGame.play(difficulty)




